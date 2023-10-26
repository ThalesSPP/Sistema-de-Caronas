import tkinter as tk


def cadastrar_participante():
    nome = nome_entry.get()
    vezes_semana = int(vezes_entry.get())
    tipo_viagem = tipo_viagem_var.get()

    with open("participantes.txt", "a") as arquivo:
        arquivo.write(f"{nome};{vezes_semana};{tipo_viagem}\n")

    status_label["text"] = "Participante cadastrado com sucesso!"


def atualizar_participante():
    nome = nome_entry.get()
    vezes_semana = int(vezes_entry.get())
    tipo_viagem = tipo_viagem_var.get()

    with open("participantes.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("participantes.txt", "w") as arquivo:
        for linha in linhas:
            if linha.startswith(nome):
                arquivo.write(f"{nome};{vezes_semana};{tipo_viagem}\n")
            else:
                arquivo.write(linha)

    status_label["text"] = "Dados do participante atualizados com sucesso!"


def calcular_custos():
    with open("participantes.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    resultados = []
    total_custo = 0  # Variável para armazenar o custo total

    for linha in linhas:
        nome, vezes_semana, tipo_viagem = linha.strip().split(";")

        if int(vezes_semana) != 0:  # Verifica se o valor de vezes_semana é diferente de zero
            if tipo_viagem == "ida":
                custo = 2.75 * int(vezes_semana)
            elif tipo_viagem == "ida_volta":
                custo = 5.5 * int(vezes_semana)

            resultados.append(f"{nome}: R$ {custo:.2f}")
            total_custo += custo

    if resultados:  # Verifica se a lista de resultados não está vazia
        # Adiciona uma linha separadora
        resultados.append("___________________________")
        # Adiciona o valor total
        resultados.append(f"Total: R$ {total_custo:.2f}")
        status_label["text"] = "\n".join(resultados)
    else:
        status_label["text"] = "Nenhum participante com valor diferente de zero."


window = tk.Tk()
window.title("CaroThales - Caronas Thales")

window_width = 500
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

font_style = ("sans-serif", 12)

linha_label = tk.Label(window, text="___________________________", font=font_style)
linha_label.pack()

nome_label = tk.Label(window, text="Nome:", font=font_style)
nome_label.pack()
nome_entry = tk.Entry(window, font=font_style)
nome_entry.pack()

vezes_label = tk.Label(window, text="Quantidade de vezes por semana:", font=font_style)
vezes_label.pack()
vezes_entry = tk.Entry(window, font=font_style)
vezes_entry.pack()

tipo_viagem_label = tk.Label(window, text="Tipo de Viagem:", font=font_style)
tipo_viagem_label.pack()
tipo_viagem_var = tk.StringVar()
tipo_viagem_var.set("ida")
tipo_viagem_ida = tk.Radiobutton(window, text="Ida/Volta", variable=tipo_viagem_var, value="ida", font=font_style)
tipo_viagem_ida.pack()
tipo_viagem_ida_volta = tk.Radiobutton(window, text="Ida e Volta", variable=tipo_viagem_var, value="ida_volta", font=font_style)
tipo_viagem_ida_volta.pack()

cadastrar_button = tk.Button(window, text="Cadastrar", command=cadastrar_participante, font=font_style)
cadastrar_button.pack()

linha_label = tk.Label(window, text="___________________________\n", font=font_style)
linha_label.pack()

atualizar_button = tk.Button(window, text="Atualizar", command=atualizar_participante, font=font_style)
atualizar_button.pack()

linha_label = tk.Label(window, text="___________________________\n", font=font_style)
linha_label.pack()

calcular_button = tk.Button(window, text="Calcular Custos", command=calcular_custos, font=font_style)
calcular_button.pack()

status_label = tk.Label(window, text="", font=font_style)
status_label.pack()

window.mainloop()
