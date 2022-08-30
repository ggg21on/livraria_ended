from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora, Livro, Autor
from core.serializers import (
    CategoriaSerializer,
    EditoraSerializer,
    LivroSerializer,
    LivroDetailSerializer,
    AutorSerializer,
)

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer