import tkinter as tk
from tkinter import messagebox

usuarios = []

# Criação da Janela Principal
janela = tk.Tk()
janela.title("Sistema de Dados")
janela.geometry("400x300")

tk.Label(janela, text="Sistema de inscrição", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

# Entrada de Nome
tk.Label(janela, text="Nome").grid(row=1, column=0)
entrar_nome = tk.Entry(janela)
entrar_nome.grid(row=1, column=1)

# Entrada de Idade
tk.Label(janela, text="Idade").grid(row=2, column=0)
entrar_idade = tk.Entry(janela)
entrar_idade.grid(row=2, column=1)

# Entrada de CPF
tk.Label(janela, text="CPF").grid(row=3, column=0)
entrar_cpf = tk.Entry(janela)
entrar_cpf.grid(row=3, column=1)

# Entrada de Endereço
tk.Label(janela, text="Endereço").grid(row=4, column=0)
entrar_endereco = tk.Entry(janela)
entrar_endereco.grid(row=4, column=1)

# Entrada de Profissão
tk.Label(janela, text="Profissão").grid(row=5, column=0)
entrar_profissao = tk.Entry(janela)
entrar_profissao.grid(row=5, column=1)


def cadastrar_usuario():
    nome = entrar_nome.get()
    idade = entrar_idade.get()
    cpf = entrar_cpf.get()
    endereco = entrar_endereco.get()
    profissao = entrar_profissao.get()

    # Verificar campos vazios
    if not nome or not idade or not cpf or not endereco or not profissao:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    # Validações específicas
    if any(char.isdigit() for char in nome):
        messagebox.showerror("Erro", "O nome não pode conter números.")
        return

    if any(char.isalpha() for char in idade):
        messagebox.showerror("Erro", "A idade não pode conter letras.")
        return

    if any(char.isalpha() for char in cpf):
        messagebox.showerror("Erro", "O CPF não pode conter letras.")
        return

    if any(char.isdigit() for char in profissao):
        messagebox.showerror("Erro", "A profissão não pode conter números.")
        return

    # Cadastro válido
    usuario = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'endereco': endereco,
        'profissao': profissao
    }

    usuarios.append(usuario)
    messagebox.showinfo("Cadastro concluído", "Seu cadastro foi efetuado com sucesso!")

    # Limpar os campos após cadastro
    entrar_nome.delete(0, tk.END)
    entrar_idade.delete(0, tk.END)
    entrar_cpf.delete(0, tk.END)
    entrar_endereco.delete(0, tk.END)
    entrar_profissao.delete(0, tk.END)


# Botão Relatório
def relatorio():
    if not usuarios:
        messagebox.showinfo("Relatório", "Nenhum usuário cadastrado ainda.")
        return

    relatorio = ""
    for u in usuarios:
        linha = (
            f"{u['nome']} tem {u['idade']} anos, CPF: {u['cpf']}, "
            f"mora em {u['endereco']} e trabalha como {u['profissao']}.\n\n"
        )
        relatorio += linha

    messagebox.showinfo("Relatório de Usuários", relatorio)


# Botões
btn_cadastrar = tk.Button(janela, text="Cadastrar", bg="yellow", command=cadastrar_usuario)
btn_cadastrar.grid(row=7, column=0, pady=10)

btn_relatorio = tk.Button(janela, text="Relatório", bg="lightgreen", command=relatorio)
btn_relatorio.grid(row=7, column=1, pady=10)

janela.mainloop()
