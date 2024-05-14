from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AdminUsuarioCustomizado(UserAdmin):
    model=UsuarioCustomizado
    list_display = ['id', 'email', 'cpf']
    list_display_links = ('id', 'email', 'cpf',)
    fieldsets = (
        (None,{'fields': ('email','password')}),
        ('Permissions', {'fields': ('is_staff','is_active','groups','user_permissions',)}),
        ('Management', {'fields': ('last_login',)}),
        ('Custom fields', {'fields': ('cpf','telefone','endereco',)}),
    )
    filter_horizontal = ('groups','user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1','password2', 'is_staff','is_active','groups','user_permissions',)
        }),
    )    
    search_fields = ['email',]
    ordering = ['email']

admin.site.register(UsuarioCustomizado,AdminUsuarioCustomizado)

class AdminCategoria(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(CategoriaProdutos,AdminCategoria)

class AdminPecas(admin.ModelAdmin):
    list_display = ['id', 'nome', 'peso', 'tamanho']
    list_display_links = ('id', 'nome', 'peso', 'tamanho',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Pecas,AdminPecas)

class AdminFoto(admin.ModelAdmin):
    list_display = ['id', 'url']
    list_display_links = ('id', 'url',)
    search_fields = ('id',)
    list_per_page = 10

admin.site.register(Foto,AdminFoto)

class AdminProdutos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'categoriaFK']
    list_display_links = ('id', 'nome', 'categoriaFK',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Produtos,AdminProdutos)


class AdminVendas(admin.ModelAdmin):
    list_display = ['id', 'usuarioFK', 'status', 'dataHora']
    list_display_links = ('id', 'usuarioFK', 'status', 'dataHora',)
    search_fields = ('usuarioFK',)
    list_per_page = 10
    
admin.site.register(Vendas,AdminVendas)

class AdminVendasProdutos(admin.ModelAdmin):
    list_display = ['id', 'produtoFK', 'quantidade', 'vendaFK']
    list_display_links = ('id', 'produtoFK', 'quantidade', 'vendaFK',)
    search_fields = ('produtoFK',)
    list_per_page = 10
    
admin.site.register(VendasProdutos,AdminVendasProdutos)