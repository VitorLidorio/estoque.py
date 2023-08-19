#estoque
import datetime 

estoque = []

def verificacao(datavalidade): #datavalidade
    vvalidade = datetime.datetime.strptime(datavalidade, "%d/%m/%Y").date()
    dia = datetime.date.today()
    if vvalidade < dia:
        print("Este produto está vencido!")
    elif vvalidade == dia:
        print("Este produto vence hoje!")
    else:
        tempo_restante = vvalidade - dia
        print(f"Faltam {tempo_restante.days} dias para o vencimento do produto.")

def cadastro(): #01 cadastrar produto
    produto = {}
    produto['nome'] = input("Digite o nome do produto: ")
    produto['informacoes'] = input("Digite quaisquer informações do produto: ")
    produto['datavalidade'] = input("Digite a data de validade do produto (dd/mm/aaaa): ")
    produto['quantidade'] = int(input("Digite a quantidade do produto: "))

    estoque.append(produto)
    print("Produto cadastrado!")
    print("---------------------------\n")

def vestoque(): #02 ver estoque
    for produto in estoque:
        print("Nome:", produto['nome'])
        print("Informações:", produto['informacoes'])
        print("Data de Validade:", produto['datavalidade'])
        print("Quantidade:", produto['quantidade'])
        verificacao(produto['datavalidade']) #datavalidade
        print("---------------------------\n")

def vproduto(nome): #03 ver produto específico
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print("Nome:", produto['nome'])
            print("Informações:", produto['informacoes'])
            print("Data de Validade:", produto['datavalidade'])
            print("Quantidade:", produto['quantidade'])
            verificacao(produto['datavalidade']) #datavalidade
            print("---------------------------\n")
            return

    print("O produto não foi encontrado!") #ERROR
    print("---------------------------\n")

def alterar(nome): #04 alterar informações do produto
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print("Produto encontrado no estoque. Digite as novas informações:")
            produto['nome'] = input("Digite o novo nome do produto: ")
            produto['informacoes'] = input("Digite as novas informações do produto: ")
            produto['datavalidade'] = input("Digite a nova data de validade do produto (no formato dd/mm/aaaa): ")
            produto['quantidade'] = int(input("Digite a nova quantidade do produto: "))

            print("Produto atualizado!")
            print("---------------------------\n")
            return

    print("Produto não encontrado!") #ERROR
    print("---------------------------\n")


while True:
    print("Bem-vindo ao sistema de gerenciamento de estoque!")
    print("Selecione uma opção:")
    print("-------------------------------------")
    print("1 - Cadastrar um produto no estoque")
    print("-------------------------------------")
    print("2 - Visualizar o estoque")
    print("-------------------------------------")
    print("3 - Visualizar um produto específico")
    print("-------------------------------------")
    print("4 - Alterar informações de um produto")
    print("-------------------------------------")
    print("5 - Sair e limpar o sistema\n")

    opcao = input("Opção selecionada: ")

    if opcao == '1': #01
        cadastro()
    elif opcao == '2': #02
        if len(estoque) == 0:
            print("Não há produtos cadastrados no estoque!") #ERROR
            print("---------------------------\n")
        else:
            vestoque()
    elif opcao == '3': #03
        nomeproduto = input("Digite o nome do produto: ")
        vproduto(nomeproduto)
    elif opcao == '4': #04
        nomeproduto = input("Digite o nome do produto: ")
        alterar(nomeproduto)
    elif opcao == '5': #05
        print("Saindo e limpando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.\n") #ERROR