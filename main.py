import os

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

def voltar_menu():
    input("Pressione Enter para voltar ao menu principal...")
    limpa_tela()

titulo = "SISTEMA DE CONTROLE FINANCEIRO"
print("========================================")
print(f"        {titulo}        ")
print("========================================")


while True:
    try:
        print("[1] - Registrar receita")
        print("[2] - Registrar despesa")
        print("[3] - Consultar saldo")
        print("[4] - Listar transações")
        print("[5] - Sair")
        print("========================================")

        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            descricao = input("Qual a descrição da receita? ")
            valor = float(input("Qual o valor da receita? "))
            print(f"Você selecionou: Registrar receita! Descrição: {descricao}, Valor: {valor}")
        elif opcao_escolhida == 2:
            descricao = input("Qual a descrição da despesa? ")
            valor = float(input("Qual o valor da despesa? "))
            print(f"Você selecionou: Registrar despesa! Descrição: {descricao}, Valor: {valor}")
        elif opcao_escolhida == 3:
            print("Você selecionou: Consultar saldo! Essa funcionalidade estará disponível em breve.")
        elif opcao_escolhida == 4:
            print("Você selecionou: Listar transações! Essa funcionalidade estará disponível em breve.")
        elif opcao_escolhida == 5:
            print("Saindo do programa...")  
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            continue
        break
   
    except ValueError:
        limpa_tela()
        print("Entrada inválida. Por favor, digite um número inteiro correspondente a uma opção.")
        voltar_menu()

        

