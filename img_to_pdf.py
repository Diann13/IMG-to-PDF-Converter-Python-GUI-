from tkinter import Tk, Button, filedialog, messagebox
from PIL import Image
import os


def convert_to_pdf():
    file_paths = filedialog.askopenfilenames(
        title="Pilih gambar",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not file_paths:
        return

    output_folder = filedialog.askdirectory(title="Pilih folder penyimpanan PDF")

    if not output_folder:
        return

    success_count = 0

    for path in file_paths:
        try:
            img = Image.open(path).convert("RGB")

            # nama PDF = nama file gambar
            file_name = os.path.splitext(os.path.basename(path))[0]
            save_path = os.path.join(output_folder, file_name + ".pdf")

            img.save(save_path)
            success_count += 1

        except Exception as e:
            messagebox.showerror("Error", f"Gagal convert:\n{os.path.basename(path)}\n\n{e}")

    messagebox.showinfo(
        "Selesai",
        f"Berhasil membuat {success_count} file PDF di folder yang dipilih 🎉"
    )


root = Tk()
root.title("IMG ke PDF Converter (1 Gambar = 1 PDF)")
root.geometry("360x180")

btn = Button(root, text="Pilih Gambar & Convert ke PDF", command=convert_to_pdf)
btn.pack(expand=True, padx=20, pady=30)

root.mainloop()