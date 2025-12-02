import random
import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
from statistics import mean
def generate_numbers():
    try:
        N = int(entry_N.get())
        if N <= 0:
            raise ValueError
    except:
        messagebox.showerror("Chyba", "Zadajte správne číslo N!")
        return
    numbers = [random.randint(-200, 200) for _ in range(N)]
    if abs_var.get() == 1:
        numbers = [abs(x) for x in numbers]
    avg_value = mean(numbers)
    output.delete("1.0", tk.END)
    output.insert(tk.END, "\n".join(map(str, numbers)))
    avg_label.config(text=f"Priemer: {avg_value}")
    plt.figure()
    plt.plot(numbers, marker="o", color="royalblue")
    plt.title("Graf generovaných hodnôt")
    plt.xlabel("Index")
    plt.ylabel("Hodnota")
    plt.grid(True)
    plt.show()
def save_to_file():
    data = output.get("1.0", tk.END).strip()
    if not data:
        messagebox.showwarning("Upozornenie", "Nie je čo uložiť!")
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Textový súbor", "*.txt"), ("Všetky súbory", "*.*")]
    )
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write("Vygenerované hodnoty:\n")
            f.write(data + "\n\n")
            f.write(avg_label.cget("text"))
        messagebox.showinfo("Hotovo", "Súbor bol uložený!")
root = tk.Tk()
root.title("Generátor čísel")
root.geometry("430x500")
root.resizable(False, False)
logo_img = tk.PhotoImage(width=1, height=1)  
root.iconphoto(False, logo_img)
main_frame = tk.Frame(root, bg="#f4f4f8", bd=2, relief="groove")
main_frame.pack(padx=15, pady=15, fill="both", expand=True)
tk.Label(main_frame, text="Generátor čísel", font=("Segoe UI", 16, "bold"), bg="#f4f4f8").pack(pady=5)
input_frame = tk.Frame(main_frame, bg="#f4f4f8")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Zadajte N:", font=("Segoe UI", 12), bg="#f4f4f8").grid(row=0, column=0, padx=5)
entry_N = tk.Entry(input_frame, font=("Segoe UI", 12), width=10)
entry_N.grid(row=0, column=1, padx=5)
abs_var = tk.IntVar()
tk.Checkbutton(main_frame, text="Použiť absolútnu hodnotu", variable=abs_var,
               font=("Segoe UI", 11), bg="#f4f4f8").pack(pady=5)
btn_frame = tk.Frame(main_frame, bg="#f4f4f8")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Generovať", font=("Segoe UI", 11), bg="#4CAF50", fg="white",
          activebackground="#45a049", width=12, command=generate_numbers).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Uložiť do súboru", font=("Segoe UI", 11), bg="#2196F3", fg="white",
          activebackground="#1976D2", width=12, command=save_to_file).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Ukončiť", font=("Segoe UI", 11), bg="#f44336", fg="white",
          activebackground="#d32f2f", width=12, command=root.quit).grid(row=0, column=2, padx=5)
output = tk.Text(main_frame, height=12, width=40, font=("Consolas", 10))
output.pack(pady=10)
avg_label = tk.Label(main_frame, text="Priemer:", font=("Segoe UI", 12), bg="#f4f4f8")
avg_label.pack(pady=5)
root.mainloop()