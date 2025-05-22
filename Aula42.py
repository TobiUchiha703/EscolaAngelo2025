import tkinter as tk
janela = None

def interface():
    rotulo = tk.Label(janela, text="Tarefa")
    rotulo.pack(pady=10)
    tarefa = tk.Entry(janela, width=70)
    tarefa.pack(pady=0,10 padx=20)

    bt_adicionar = tk.Button(janela, text='Adicionar Tarefa')


def main():
    janela = tk.Tk()
    janela.title("Gerenciador de Tarefas")
    interface()
    janela.mainloop()
    
main()