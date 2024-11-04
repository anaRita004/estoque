estoque = {"Arroz": 50, "Feijão": 30, "Macarrão": 40}

while True:
    print("\n-----🏪 Controle de Estoque 📦-----")
    print("1. Adicionar produto ➕")
    print("2. Remover produto 🗑️")
    print("3. Atualizar quantidade 🔢")
    print("4. Exibir estoque 📊")
    print("5. Sair 🔸")

    opcao = input("Escolha uma opção: ")
    print(50 * '-')

    if opcao == "1":
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a ser adicionada: "))
        estoque[produto] = estoque.get(produto, 0) + quantidade
        print("Produto adicionado com sucesso!✅")
    elif opcao == "2":
        produto = input("Digite o nome do produto para remover: ")
        if produto in estoque:
            del estoque[produto]
            print("Produto removido com sucesso!✅")
        else:
            print("Produto não encontrado no estoque. Tente novamente.")
    elif opcao == "3":
        produto = input("Digite o nome do produto para atualizar a quantidade: ")
        if produto in estoque:
            quantidade = int(input("Digite a nova quantidade: "))
            estoque[produto] = quantidade
            print("Quantidade atualizada com sucesso!✅")
        else:
            print("Produto não encontrado no estoque. Tente novamente.")
    elif opcao == "4":
        print("Estoque atual:")
        for produto, quantidade in estoque.items():
            print("{}: {}".format(produto, quantidade))
    elif opcao == "5":
        print("Encerrando programa... Até mais!👋")
        break
    else:
        print("Opção inválida. Tente novamente.")