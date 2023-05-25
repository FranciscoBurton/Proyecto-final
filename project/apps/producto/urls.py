from django.urls import path

from . import views

# *********** URLS basadas en funciones
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("producto_categoria_listado/", views.producto_categoria_list, name="producto_categoria_list"),
#     path("producto_categoria_create/", views.producto_categoria_create, name="producto_categoria_create"),
#     path("producto_categoria_delete/<int:id>", views.producto_categoria_delete, name="producto_categoria_delete"),
#     path("producto_categoria_update/<int:id>", views.producto_categoria_delete, name="producto_categoria_delete"),
# ]

# *********** URLS basadas en clases
urlpatterns = [
    path("", views.index, name="index"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/create/", views.ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
    path(
        "productocategoria/delete/<int:pk>", views.ProductoCategoriaDelete.as_view(), name="productocategoria_delete"
    ),
    # ! De forma predeterminada, las URLs basadas en clases reciben pk, no id.
    path(
        "productocategoria/update/<int:pk>", views.ProductoCategoriaUpdate.as_view(), name="productocategoria_update"
    ),
]
