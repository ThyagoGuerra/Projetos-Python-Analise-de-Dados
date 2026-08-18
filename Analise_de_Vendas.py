import numpy as np

lista_vendas = np.array([{"Produto": "Iphone 16", 
                        "Catergoria":"Eletrônico", 
                        "Vendedor": "Thyago Guerra", 
                        "Quantidade": 2, 
                        "Preço": 4345},
                        {"Produto": "Notebook", "Catergoria": "Eletrônico", "Vendedor": "Kauê Amaral", "Quantidade": 1, "Preço": 5234},
                        {"Produto": "Lego", "Catergoria": "Brinquedo", "Vendedor": "Kauê Amaral", "Quantidade": 4, "Preço": 3345},
                        {"Produto": "Bicicleta", "Catergoria": "Veiculo", "Vendedor": "Thyago Guerra", "Quantidade": 1, "Preço": 789},
                        {"Produto": "Iphone 16", "Catergoria": "Eletrônico", "Vendedor": "Bruno Andrade", "Quantidade": 4, "Preço": 4345}])

def faturamento(lista_vendas):
    # Percorre os valores dentro do dicionário (Utilizando o List Comprehesion)
    quantidade = np.array([qntd["Quantidade"]
                        for qntd in lista_vendas])
    # Percorre os valores dentro do dicionário (Utilizando o List Comprehesion)
    precos = np.array([preco["Preço"]
                    for preco in lista_vendas])

    faturamento_geral = quantidade * precos
    faturamento_total = np.sum(faturamento_geral)
    print(f"Faturamento: R$ {faturamento_total}")

faturamento(lista_vendas)

def quantidade_vendida(lista_vendas):
    # Percorre os valores dentro do dicionário (Utilizando o List Comprehesion)
    quantidade = np.array([qntd["Quantidade"]
                        for qntd in lista_vendas])

    quantidade_total = np.sum(quantidade)
    print(f"Quantidade Total: {quantidade_total}")

quantidade_vendida(lista_vendas)

def produto_vendido(lista_vendas):
    # Dicionário - utilizado para armazenar o agrupomento
    contagem = {}
    # Percorre cada venda da lista
    for vendas in lista_vendas:
        produto = vendas["Produto"]
        quantidade = vendas["Quantidade"]

        # Agrupamento dos produtos e acumula a quantidade
        if produto in contagem:
            contagem[produto] += quantidade
        else:
            contagem[produto] = quantidade

    # values() - Valores dentro de contagem
    # max() - Encontra o maior valor entre as quantidades
    maior_quantidade = max(contagem.values())
    produto_mais_vendido = max(
        contagem,
        # key - Critério utilizado o max()
        # get - Obtém os valores associados a cada chave
        key=contagem.get
    )

    print("\nProduto mais vendido:")
    print(f"Produto: {produto_mais_vendido}, Quantidade: {maior_quantidade}")

produto_vendido(lista_vendas)

def produto_faturamento(lista_vendas):
    # Dicionário - utilizado para armazenar o agrupomento
    contagem = {}
    # Percorre cada faturamento da lista
    for faturamento in lista_vendas:
        produto = faturamento["Produto"]
        quantidade = faturamento["Quantidade"]
        precos = faturamento["Preço"]

        faturamento_geral = quantidade * precos

        # Agrupamento dos produtos e acumula o faturamentos
        if produto in contagem:
            contagem[produto] += faturamento_geral
        else:
            contagem[produto] = faturamento_geral

    # values() - Valores dentro de contagem
    # max() - Encontra o maior valor entre as quantidades
    maior_faturamento = max(contagem.values())
    produto_maior_faturamento = max(
        contagem,
        # key - Critério utilizado o max()
        # get - Obtém os valores associados a cada chave
        key=contagem.get)

    print("\nProduto com maior faturamento:")
    print(f"Produto: {produto_maior_faturamento}, R$ {maior_faturamento:.2f}")

produto_faturamento(lista_vendas)

def vendedor_faturamento(lista_vendas):
    # Dicionário - utilizado para armazenar o agrupomento
    contagem = {}
    # Percorre cada faturamento da lista
    for faturamento in lista_vendas:
        vendedor = faturamento["Vendedor"]
        quantidade = faturamento["Quantidade"]
        preco = faturamento["Preço"]

        faturamento_geral = quantidade * preco

        # Agrupamento dos vendedores e acumula o faturamento
        if vendedor in contagem:
            contagem[vendedor] += faturamento_geral
        else:
            contagem[vendedor] = faturamento_geral

    # values() - Valores dentro de contagem
    # max() - Encontra o maior valor entre as quantidades
    maior_faturamento = max(contagem.values())
    vendedor_maior_faturamento = max(
        contagem,
        # key - Critério utilizado o max()
        # get - Obtém os valores associados a cada chave
        key=contagem.get
    )

    print("\nVendedor com maior faturamento:")
    print(f"Vendedor: {vendedor_maior_faturamento}, R$ {maior_faturamento:.2f}")

vendedor_faturamento(lista_vendas)

def ticket_medio(lista_vendas):
    total = 0
    # faturamento e produtos - Listas
    faturamento = []
    produtos = []
    # Percorre cada ticket da lista
    for ticket in lista_vendas:
        produto = ticket["Produto"]
        quantidade = ticket["Quantidade"]
        preco = ticket["Preço"]

        faturamento_geral = quantidade * preco

        # Adicionado os valores pora a lista
        faturamento.append(faturamento_geral)
        produtos.append(produto)

        total += faturamento_geral

    ticket_medio = total / len(lista_vendas)
    print()
    print(f"Ticket Médio: R$ {ticket_medio:.2f}\n")

    print("Produtos acima da média:")
    # zip - Combina os elementos das listas pela mesma posição
    for produto, maior in zip(produtos, faturamento):
        if maior > ticket_medio:
            print(f"Produto: {produto} -> R$ {maior}")

ticket_medio(lista_vendas)