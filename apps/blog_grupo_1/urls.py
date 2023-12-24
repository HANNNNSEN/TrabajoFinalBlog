from django.urls import path
from .views import InicioListView, NosotrosTemplateView,PerfilTemplateView, ContactoFormView, ContactoTemplateView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ComentarioCreateView, ComentarioDeleteView, CategoriaListView, UserListView

app_name = 'apps.blog_grupo_1'

urlpatterns = [
    path(
        route='',
        view=InicioListView.as_view(),
        name='inicio'
    ),
    path(
        route='nosotros/',
        view=NosotrosTemplateView.as_view(),
        name='nosotros'
    ),
    path(
        route='perfil/',
        view=PerfilTemplateView.as_view(),
        name='perfil'
    ),
    path(
        route='contacto/',
        view=ContactoFormView.as_view(),
        name='contacto'
    ),
    path(
        route='contactook/',
        view=ContactoTemplateView.as_view(),
        name='contactook'
    ),
    path(
        route='post/<slug:url>/',
        view=PostDetailView.as_view(),
        name='detalle'
    ),
    path(
        route='carga_post/',
        view=PostCreateView.as_view(),
        name='carga_post'
    ),
    path(
        route='actualizar_post/<slug:url>/',
        view=PostUpdateView.as_view(),
        name='actualizar_post'
    ),
    path(
        route='eliminar_post/<slug:url>/',
        view=PostDeleteView.as_view(),
        name='eliminar_post'
    ),
    path(
        route='comentario/',
        view=ComentarioCreateView.as_view(),
        name='comentario'
    ),
    path(
        route='eliminar_comentario/<int:pk>/',
        view=ComentarioDeleteView.as_view(),
        name='eliminar_comentario'
    ),
    path(
        route='categoria/<int:categoria_id>/',
        view=CategoriaListView.as_view(),
        name='categoria'
    ),
    path(
        route='user/<str:nombre>/',
        view=UserListView.as_view(),
        name='user'
    ),

]
