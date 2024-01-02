# Project DDP tkinter Kelompok 5 (Aplikasi Konversi Mata Uang)
# Nama Anggota : 
# 1. Muhammad Umam Afif
# 2. Muhammad Fikrie El Muqoffa
# 3. Muhammad Fatih Ikhlasul Amal

import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class Konversimatauangapp:
    def __init__(self, aplikasi):
        self.aplikasi = aplikasi
        self.aplikasi.title("Aplikasi Konversi Mata Uang") # Memberikan Judul/Title 

        self.label_nilai = tk.Label(aplikasi, text="Masukan Nilai :") # Memberikan Label 
        self.label_nilai.grid(row=0, column=0, padx=10, pady=10) # Mengatur Jarak Label
        self.label_nilai.config(background="#6B240C", foreground="#EAD196", font="Georgia") # Mengatur Background, Warna Font, dan Font yang digunakan

        self.masukan_nilai = tk.Entry(aplikasi) # Memberikan tempat untuk Input nilai/ entry
        self.masukan_nilai.grid(row=0, column=1, padx=10, pady=10 ) # Mengatur Jarak
        self.masukan_nilai.config(width="23") # Mengatur Panjang entry

        self.label_dari_matauang = tk.Label(aplikasi, text="Dari Mata Uang :") # Memberikan Label 
        self.label_dari_matauang.grid(row=1, column=0, padx=10, pady=10,) # Mengatur Jarak Label
        self.label_dari_matauang.config(background="#6B240C", foreground="#EAD196", font="Georgia") # Mengatur Background, Warna Font, dan Font yang digunakan

        self.matauang_dari_var = tk.StringVar() 
        self.matauang_dari_combobox = ttk.Combobox(aplikasi, textvariable=self.matauang_dari_var) # Membuat Combobox
        self.matauang_dari_combobox.grid(row=1, column=1, padx=10, pady=10) # Mengatur Jarak

        self.matauang_ke_label = tk.Label(aplikasi, text="Konversi ke :")
        self.matauang_ke_label.grid(row=2, column=0, padx=10, pady=10) # Mengatur Jarak
        self.matauang_ke_label.config(background="#6B240C", foreground="#EAD196", font="Georgia") # Mengatur Background, Warna Font, dan Font yang digunakan

        self.matauang_ke_var = tk.StringVar()
        self.matauang_ke_combobox = ttk.Combobox(aplikasi, textvariable=self.matauang_ke_var) # Membuat Combobox
        self.matauang_ke_combobox.grid(row=2, column=1, padx=10, pady=10) # Mengatur Jarak

        self.tombol_koversi = tk.Button(aplikasi, text="Konversi", command=self.convert_currency)
        self.tombol_koversi.grid(row=3, column=0, columnspan=2, pady=10) # Mengatur Jarak

        self.label_hasil = tk.Label(aplikasi, text="") # Memberikan Label 
        self.label_hasil.grid(row=4, column=0, columnspan=2, pady=10) # Mengatur Jarak
        self.label_hasil.config(background="#6B240C", foreground="#EAD196", font="Georgia", relief="raised", bd=5, width=30) # Mengatur Background, Warna Font, dan Font yang digunakan

        self.populate_currency_combobox()

    def populate_currency_combobox(self):
        c = CurrencyRates()
        mata_uang = c.get_rates("USD")
        list_matauang = list(mata_uang.keys())

        self.matauang_dari_combobox['values'] = list_matauang
        self.matauang_dari_combobox.set("USD")

        self.matauang_ke_combobox['values'] = list_matauang
        self.matauang_ke_combobox.set("IDR")

    def convert_currency(self):
        try:
            nilai = float(self.masukan_nilai.get())
            matauang_dari = self.matauang_dari_var.get()
            matauang_ke = self.matauang_ke_var.get()

            c = CurrencyRates()
            rate = c.get_rate(matauang_dari, matauang_ke)
            hasil = round(nilai * rate, 2)

            self.label_hasil.config(text=f"Hasil: {nilai} {matauang_dari} = {hasil} {matauang_ke}")
        except ValueError:
            self.label_hasil.config(text="Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    layar = tk.Tk()
    app = Konversimatauangapp(layar)
    layar.geometry("310x250")
    layar.config(background="#6B240C")
    layar.mainloop()