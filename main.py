
def mostrar_opcoes():
  prompt = """
    Escolha uma das seguintes opções:

    1. Listar contatos
    2. Listar contatos favoritados
    3. Adicionar/Remover favorito
    4. Adicionar contato
    5. Editar contato
    6. Apagar contato
    7. Sair
  """
  print(prompt)

  opcao_selecionada = int(input('Digite uma opção: '))

  executar_opcao(opcao_selecionada)

contatos = list()

def fecha_separador():
  print('===============================')
  return

def separador(titulo):
  print(f'====== {titulo} ======')
  return

def printa_contato(indice, contato):
  print(f"{indice}. Nome: {contato['nome']} {'(Favorito)' if contato['favorito'] else ''} | Email: {contato['email']} | Telefone: {contato['telefone']}")

def listar_contatos(contatos):
  separador('Lista de contatos')

  if len(contatos) == 0:
    print('Nenhum contato adicionado')
  else:
    print('Contatos:')
    for indice, contato in enumerate(contatos, start=1):
      printa_contato(indice, contato)

  fecha_separador()

def listar_favoritos(contatos):
  separador('Contatos Favoritos')

  contador_favoritos = 0

  for indice, contato in enumerate(contatos, start=1):
    if contato['favorito']:
      printa_contato(indice, contato)
      contador_favoritos += 1

  if contador_favoritos == 0:
    print('Nenhum contato favoritado')

  fecha_separador()

def adicionar_contato(contatos):
  separador('Adicionar contato')

  contato = dict()
  contato['nome'] = input('Nome: ')
  contato['favorito'] = input('Favorito? [s/n]: ') == 's'
  contato['telefone'] = input('Telefone: ')
  contato['email'] = input('Email: ')
  
  if len(contato['nome']) == 0 or len(contato['telefone']) == 0 or len(contato['email']) == 0:
    print('Nome, telefone e email são obrigatórios!')
    return adicionar_contato(contatos)

  contatos.append(contato)
  print('Contato adicionado com sucesso!')

  fecha_separador()
      
def editar_contato(contatos):
  separador('Editar contato')
  indice = int(input('Índice do contato a ser editado: '))
  indice_corrigido = indice - 1
  
  try:
    contato = contatos[indice_corrigido]
  except IndexError:
    print(f"O índice {indice} não existe na lista.")
    fecha_separador()
    return

  printa_contato(indice_corrigido, contato)

  contato['nome'] = input('Nome: ')
  contato['favorito'] = input('Favorito? [s/n]: ') == 's'
  contato['telefone'] = input('Telefone: ')
  contato['email'] = input('Email: ')

  if len(contato['nome']) == 0 or len(contato['telefone']) == 0 or len(contato['email']) == 0:
    print('Nome, telefone e email são obrigatórios!')
    return editar_contato(contatos)

  print('Contato editado com sucesso!')
  fecha_separador()

def editar_favorito(contatos):
  separador('Adicionar/Remover favorito')
  indice = int(input('Índice do contato a adicionar/remover favorito: '))
  indice_corrigido = indice - 1

  try:
    contato = contatos[indice_corrigido]
  except IndexError:
    print(f"O índice {indice} não existe na lista.")
    fecha_separador()
    return
  
  print('Contato selecionado: ', printa_contato(indice, contato))

  contato['favorito'] = input('Favorito? [s/n]: ') == 's'
  
  print(f'Contato {'favoritado' if contato["favorito"] else 'desfavoritado'}.')

  fecha_separador()

def apagar_contato(contatos):
  separador('Apagar contato')
  indice = int(input('Indice do contato a ser apagado: '))
  indice_corrigido = indice - 1

  try:
    contato = contatos[indice_corrigido]
  except IndexError:
    print(f"O índice {indice} não existe na lista.")
    fecha_separador()
    return
  
  printa_contato(indice_corrigido, contato)
  deleta = input('Tem certeza? [s/n]: ') == 's'

  if deleta:
    contatos.remove(contatos[indice_corrigido])
    print('Contato removido!')

  fecha_separador()


def fechar_programa():
  print('Fechando o programa...')
  exit()

def executar_opcao(opcao):
  match opcao:
    case 1:
      listar_contatos(contatos)
    case 2:
      listar_favoritos(contatos)
    case 3:
      editar_favorito(contatos)
    case 4:
      adicionar_contato(contatos)
    case 5:
      editar_contato(contatos)
    case 6:
      apagar_contato(contatos)
    case 7:
      fechar_programa()
    case _:
      print('Opção inválida')

while True:
  mostrar_opcoes()