from customtkinter import *
class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x270")
        self.title("Адаптація")
        self.knopka = CTkButton(self,text = "Кнопка")
        self.knopka.place(x = 100, y = 100)
    def adaptive(self):
        self.knopka.place(x = self.winfo_width()-self.knopka.winfo_width(), y = self.winfo_height()- self.knopka.winfo_width())
        self.after(99,self.adaptive)

win = App()
win.adaptive()
win.mainloop()