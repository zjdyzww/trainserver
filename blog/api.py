from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from common.jsonrender import EmberJSONRenderer
from common.pagination import ListPagination
from django_filters.rest_framework import DjangoFilterBackend


class ArticleViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    renderer_classes = (EmberJSONRenderer,)
    queryset = Article.objects.all().order_by('-pub_time')
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser,)
    pagination_class = ListPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status',)

    def get_object(self):

        instance = super(ArticleViewSet, self).get_object()
        instance.viewed()
        return instance
