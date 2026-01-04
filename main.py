import json



def salvar_tarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as lista_tarefa:
        json.dump(tarefas, lista_tarefa, ensure_ascii=False, indent=4)

def carregar_tarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as lista_tarefa:
            return json.load(lista_tarefa)
    except FileNotFoundError:
        return []
    

def mostra_menu():
    print ("\n1 - Adicionar uma tarefa")
    print ("2 - Listar tarefas")
    print ("3 - Concluir uma tarefa")
    print ("4 - Sair\n")

def adicionar_tarefa(tarefas):
    tarefa = input("Adicione sua tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\nAqui estão suas tarefas:")
    for n, t in enumerate(tarefas, start=1):
            print(f"{n} - {t}")

def concluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para concluir.")
        return

    listar_tarefa(tarefas)

    try:
        c = int(input("\nSelecione a tarefa que deseja concluir: "))
        print(f"\nA tarefa '{tarefas[c-1]}' foi concluida e removida da sua lista")
        tarefas.remove(tarefas[c-1])
    except (ValueError, IndexError):
         print("Opção inválida")

def main():
    tarefas = carregar_tarefas()

    

    while True:
        mostra_menu()

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if opcao == 1:
            adicionar_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == 2:
            listar_tarefa(tarefas)
        elif opcao == 3:
            concluir_tarefa(tarefas)
            salvar_tarefas(tarefas)
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

main()