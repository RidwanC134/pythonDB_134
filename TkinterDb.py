import sqlite3
import tkinter as tk

# Membuat koneksi dan menambahkan penyimpanan data ke database SQLite
conn = sqlite3.connect('TkinterDb.db')
c = conn.cursor()

# Membuat tabel nilai_siswa
# Membuat atribut nama_siswa, biologi, fisika, inggris, dan prediksi_fakultas
c.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
             (nama_siswa text, Biologi INTEGER, Fisika INTEGER, Inggris INTEGER, prediksi_fakultas text)''')

# Membuat fungsi def_prediksi fakultas(biologi, fisika, inggris): untuk menentukan prodi yang diinginkan 
# Membuat kondisi untuk nilai yang berbeda untuk setiap pilihan prodi yang diinginkan :
# 1. Jika nilai Biologi paling tinggi, maka hasil prediksi = Kedokteran
# 2. Jika nilai Fisika paling tinggi, maka hasil prediksi  = Teknik
# 3. Selain keduanya, maka hasil prediksi                  = Bahasa
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    else:
        return "Bahasa"

# Membuat fungsi def simpan_data(): untuk menyimpan data ke database SQLite
def simpan_data():
    nama = entry_nama.get() # Mengambil nilai inputan entry_nama menggunakan .get() kemudian disimpan di variable nama
    biologi = int(entry_biologi.get()) # Mengambil nilai inputan pada entry menggunakan .get(), lalu dikonversi ke integer, kemudian disimpan ke setiap variablenya
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())
    prediksi = prediksi_fakultas(biologi, fisika, inggris)
    c.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?)", (nama, biologi, fisika, inggris, prediksi)) # Menambahkan data ke dalam tabel nlai_siswa di database SQLite
    conn.commit() # Mengonfirmasi setiap perubahan penyisipan data, penghapusan, atau pembaruan yang dilakukan pada database SQLite
    entry_nama.delete(0, tk.END) # Menghapus nilai inputan di dalam entry setelah mengklik submit, agar dapat melakukan inputan selanjutnya
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

# Membuat GUI menggunakan tkinter
window = tk.Tk()
window.geometry("300x200")
window.resizable(False,False)
window.title("Input Nilai Siswa")

# Membuat label dan entry untuk nama siswa
label_nama = tk.Label(window, text="  Nama Siswa")
label_nama.grid(row=0, column=0, padx=5, pady=5)
entry_nama = tk.Entry(window)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

# Membuat label dan entry untuk nilai biologi
label_biologi = tk.Label(window, text="  Nilai Biologi")
label_biologi.grid(row=1, column=0, padx=5, pady=5)
entry_biologi = tk.Entry(window)
entry_biologi.grid(row=1, column=1, padx=5, pady=5)

# Membuat label dan entry untuk nilai fisika
label_fisika = tk.Label(window, text="Nilai Fisika")
label_fisika.grid(row=2, column=0, padx=5, pady=5)
entry_fisika = tk.Entry(window)
entry_fisika.grid(row=2, column=1, padx=5, pady=5)

# Membuat label dan entry untuk nilai inggris
label_inggris = tk.Label(window, text="  Nilai Inggris")
label_inggris.grid(row=3, column=0, padx=5, pady=5)
entry_inggris = tk.Entry(window)
entry_inggris.grid(row=3, column=1, padx=5, pady=5)

# Membuat tombol submit
button_submit = tk.Button(window, text="Submit", command=simpan_data) # Untuk menjalankan fungsi simpan_data setelah mengklik button Submit
button_submit.grid(row=4, column=1, padx=5, pady=5)

window.mainloop()