import tkinter as tk
from tkinter import messagebox
import ipaddress

def calculate():
    try:
        ip=ip_entry.get()
        subnet = subnet_entry.get()

        network = ipaddress.ip_network(f"{ip}/{subnet}", strict=False)

        hosts = list(network.hosts())

        result_text.set(
            f"Network: {network.network_address}\n"
            f"Broadcast: {network.broadcast_address}\n"
            f"First Host: {hosts[0] if hosts else 'N/A'}\n"
            f"Last Host: {hosts[-1] if hosts else 'N/A'}\n"
            f"Total Hosts: {network.num_addresses - 2 if network.num_addresses > 2 else 0}"
        )

    except Exception:
        messagebox.showerror("Error", "Invalid IP or Subnet")

def copy_result():
    root.clipboard_clear()
    root.clipboard_append(result_text.get())
    root.update()

root = tk.Tk()
root.title("Subnet Pro")
root.geometry("400x300")
root.configure(bg="#1e1e1e")

tk.Label(root,text="Subnet Pro", fg="white",bg="#1e1e1e",
    font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

tk.Label(frame, text="IP Address", fg="white", bg="#1e1e1e").grid(row=0, column=0, padx=5)
ip_entry = tk.Entry(frame, width=20)
ip_entry.grid(row=0, column=1)

tk.Label(frame, text="Subnet Mask / CIDR", fg="white", bg="#1e1e1e").grid(row=1, column=0, padx=5)
subnet_entry = tk.Entry(frame, width=20)
subnet_entry.grid(row=1, column=1)

tk.Button(root, text="Calculate", command=calculate, bg="#007acc", fg="white").pack(pady=5)
tk.Button(root, text="Copy result", command=copy_result).pack(pady=5)

result_text = tk.StringVar()
output = tk.Label(root, textvariable=result_text, fg="white", bg="#1e1e1e",
            justify="left", font=("Consolas", 10))
output.pack(pady=10)

root.mainloop()