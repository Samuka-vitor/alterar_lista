# lista de nomes 
nomes = ["Alex", "Leão", "Fulano", "Arroba da Silva", "João", "Maria", "Vitor"]

# exibe a lista original
for i in range(len(nomes)):
        print (f"Índice {i}: {nomes[i]}")

# usuário informa o índice que deseja alterar 
try:
    indice = int(input("Informa o nome que deseja alterar: "))
    confirmacao = input (f"Deseja alterar o nome {nomes[indice]}? Digite 'sim' para confirmar.")

    if confirmacao == "sim":
        novo_nome = input("Informe o novo nome: ")
        nomes[indice] = novo_nome

    else:
        ...

except Exception as e: 
    print(f"Não foi possível alterar o nome. {e}.")

finally: 
     # exibe a lista original
    for i in range(len(nomes)):
        print (f"Índice {i}: {nomes[i]}")

