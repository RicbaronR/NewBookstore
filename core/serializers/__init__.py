from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .livro import LivroRetrieveSerializer, LivroSerializer, LivroListSerializer
from .user import UserRegistrationSerializer, UserSerializer
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer, # novo
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, # novo
    ItensCompraSerializer,
)