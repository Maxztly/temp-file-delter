import os
import shutil
import tkinter as tk

def delete_temp_files():
    temp_directory = os.path.join(os.environ.get('TEMP'), '')

    for file in os.listdir(temp_directory):
        file_path = os.path.join(temp_directory, file)

        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Erfolgreich gelöscht: {file_path}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Erfolgreich gelöscht: {file_path}")
        except Exception as e:
            print(f"Fehler beim Löschen von {file_path}: {str(e)}")

def create_gui():
    root = tk.Tk()
    root.title("Temporäre Dateien löschen")

    window_width = 300
    window_height = 100

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    button = tk.Button(root, text="Temporäre Dateien löschen", command=delete_temp_files)
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
