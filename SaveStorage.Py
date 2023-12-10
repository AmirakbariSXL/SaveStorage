import tkinter as tk

class StorageGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Storage System By Pythonism-SXL")
        self.storage = Storage()

        # Create input fields
        tk.Label(self.master, text="Name").grid(row=0, column=0)
        tk.Label(self.master, text="Amount").grid(row=0, column=1)
        tk.Label(self.master, text="Quantity").grid(row=0, column=2)
        self.name_entry = tk.Entry(self.master)
        self.amount_entry = tk.Entry(self.master)
        self.quantity_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=0)
        self.amount_entry.grid(row=1, column=1)
        self.quantity_entry.grid(row=1, column=2)

        # Create buttons
        tk.Button(self.master, text="Add Goods", command=self.add_goods).grid(row=2, column=0)
        tk.Button(self.master, text="Remove Goods", command=self.remove_goods).grid(row=2, column=1)
        tk.Button(self.master, text="Get Goods", command=self.get_goods).grid(row=2, column=2)

        # Create output field
        self.output = tk.Text(self.master, height=10, width=50)
        self.output.grid(row=3, column=0, columnspan=3)

    def add_goods(self):
        name = self.name_entry.get()
        amount = int(self.amount_entry.get())
        quantity = int(self.quantity_entry.get())
        self.storage.add_goods(name, amount, quantity)
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, f"{name} added to storage system.\n")

    def remove_goods(self):
        name = self.name_entry.get()
        amount = int(self.amount_entry.get())
        quantity = int(self.quantity_entry.get())
        if self.storage.remove_goods(name, amount, quantity):
            self.output.delete('1.0', tk.END)
            self.output.insert(tk.END, f"{amount} {name}(s) removed from storage system.\n")
        else:
            self.output.delete('1.0', tk.END)
            self.output.insert(tk.END, f"Not enough {name} in storage system.\n")

    def get_goods(self):
        goods = self.storage.get_goods()
        self.output.delete('1.0', tk.END)
        for name, info in goods.items():
            self.output.insert(tk.END, f"{name}: {info['amount:']} ({info['quantity:']})\n")

root = tk.Tk()
app = StorageGUI(root)
root.mainloop()
