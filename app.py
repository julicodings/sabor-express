import os
import platform # Importa o módulo platform para verificar o sistema operacional

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def limpar_tela():
  ''' Limpa a tela do console de forma multiplataforma '''
  sistema_operacional = platform.system()
  if sistema_operacional == 'Windows':
    os.system('cls')
  else:
    os.system('clear')

def exibir_nome_do_programa():
  ''' Essa função é responsável por o nome estilizado do programa na tela'''
  print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
  ''' Essa função é responsável por exibir as opções do menu principal'''
  print('1. Cadastrar restaurante')
  print('2. Listar restaurantes')
  print('3. Alternar estado do restaurante')
  print('4. Sair\n')

def finalizar_app():
  ''' Essa função é responsável por exibir a mensagem de finalização do app'''
  exibir_subtitulo('Finalizando o app...')
  # A saída agora é controlada pelo loop no main

def voltar_ao_menu_principal():
  ''' Essa função é responsável por pausar e permitir voltar ao menu principal
  '''
  input('\nDigite uma tecla para voltar ao menu ')
  # Não chama mais main() aqui, apenas retorna para o loop principal

def opcao_invalida():
  ''' Essa função é responsável por indicar uma opção inválida e retorna ao menu principal
  Outputs:
  - Exibe mensagem de opção inválida e pausa para voltar ao menu.
  '''
  print('Opção inválida!\n')
  voltar_ao_menu_principal()

def exibir_subtitulo(texto):
  ''' Exibe um subtítulo estilizado na tela

  Inputs:
  - texto: str - O texto do subtítulo
  '''
  limpar_tela() # Usa a função multiplataforma
  linha = '*' * (len(texto))
  print(linha)
  print(texto)
  print(linha)
  print()

def cadastrar_novo_restaurante():
  ''' Essa função é responsável por cadastrar um novo restaurante

  Inputs:
  - Nome do Restaurante
  - Categoria

  Outputs:
  - Adiciona um novo restaurante a lista de restaurantes
  '''
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
  categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
  dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria,'ativo':False}
  restaurantes.append(dados_do_restaurante)
  print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

  voltar_ao_menu_principal()

def listar_restaurantes():
  ''' Lista os restaurantes presentes na lista

  Outputs:
  - Exibe a lista de restaurantes na tela
  '''
  exibir_subtitulo('Listando restaurantes')

  print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = 'ativado' if restaurante['ativo']else 'desativado'
    print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

  voltar_ao_menu_principal()

def alternar_estado_restaurante():
  ''' Altera o estado ativo/desativado de um restaurante

  Outputs:
  - Exibe mensagem indicando o sucesso da operação ou que não foi encontrado.
  '''
  exibir_subtitulo('Alterando estado do restaurante')
  nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo']
      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)
      break # Adiciona break para sair do loop após encontrar e alterar

  if not restaurante_encontrado:
    print('O restaurante não foi encontrado')

  voltar_ao_menu_principal()


def escolher_opcao():
  ''' Solicita e executa a opção escolhida pelo usuário

  Outputs:
  - Executa a opção escolhida pelo usuário
  - Retorna True se o programa deve continuar, False se deve sair.
  '''
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      alternar_estado_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
      return False # Sinaliza para sair do loop principal
    else:
      opcao_invalida()
  except ValueError: # Captura especificamente o erro de conversão para int
    opcao_invalida()

  return True # Sinaliza para continuar o loop principal

def main():
  ''' Função principal que executa o loop do programa'''
  while True: # Loop principal do programa
    limpar_tela()
    exibir_nome_do_programa()
    exibir_opcoes()
    continuar = escolher_opcao()
    if not continuar:
      break # Sai do loop se escolher_opcao retornar False

if __name__ == '__main__':
  main()