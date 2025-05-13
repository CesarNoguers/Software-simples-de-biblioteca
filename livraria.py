# Software para gerenciamento de uma livraria

# Catálogo inicial de livros
catalogo = [
    {"id": 1, "titulo": "Dom Quixote", "autor": "Miguel de Cervantes"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"},
    {"id": 3, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
]

# Função para listar todos os livros
def listar_livros():
    if not catalogo:
        print("O catálogo está vazio.")
    else:
        print("Livros no catálogo:")
        for livro in catalogo:
            print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}")

# Função para adicionar um livro
def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    novo_id = max([livro['id'] for livro in catalogo], default=0) + 1
    catalogo.append({"id": novo_id, "titulo": titulo, "autor": autor})
    print(f"Livro '{titulo}' adicionado com sucesso!")

# Função para remover um livro
def remover_livro():
    try:
        id_livro = int(input("Digite o ID do livro a ser removido: "))
        for livro in catalogo:
            if livro['id'] == id_livro:
                catalogo.remove(livro)
                print(f"Livro '{livro['titulo']}' removido com sucesso!")
                return
        print("Livro não encontrado.")
    except ValueError:
        print("Por favor, insira um ID válido.")

# Menu principal
def menu():
    while True:
        print("\n=== Sistema de Gerenciamento de Livros ===")
        print("1. Listar todos os livros")
        print("2. Adicionar um novo livro")
        print("3. Remover um livro")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            adicionar_livro()
        elif opcao == "3":
            remover_livro()
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()