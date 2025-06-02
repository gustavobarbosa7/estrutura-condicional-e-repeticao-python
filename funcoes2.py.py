def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Testes
loginUsuario('Admin')
loginUsuario('user')
loginUsuario('ADMIN')
loginUsuario('usuário')
