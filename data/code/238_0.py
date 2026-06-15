import tkinter as tk
def create_box(master, x1, y1, x2, y2, fill_color):
    canvas = tk.Canvas(master, width=300, height=200, bg="white")
    canvas.pack()
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Simple Canvas Box")
    create_box(root, 50, 50, 250, 150, "lightblue")
    root.mainloop()