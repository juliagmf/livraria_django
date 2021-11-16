"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views #arquivo views que ainda não utilizamos

# para listar os livros
urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('listar_categorias', views.listar_categorias, name='listar_categorias'), 
    path('listar_autores', views.listar_autores, name='listar_autores'), 
    path('livro/<int:id>/', views.detalhar_livro, name='detalhar_livro'),
    path('livro/new/', views.cadastrar_livro, name='cadastrar_livro'),
    path('livro/editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('buscar_livro', views.buscar_livro, name='buscar_livro'),
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]