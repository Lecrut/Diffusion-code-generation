import tkinter as tk
def create_box_design():
    root = tk.Tk()
    root.title("Canvas Box Design")
    canvas_width = 400
    canvas_height = 300
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=10, pady=10)
    x1, y1 = 50, 50
    x2, y2 = 350, 250
    color1 = "lightblue"
    color2 = "lightgreen"
    canvas.create_rectangle(x1, y1, x2, y2, fill=color1, outline="black")
    canvas.create_rectangle(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=color2, outline="black")
    root.mainloop()
if __name__ == '__main__':
    create_box_design()