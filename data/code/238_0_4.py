import tkinter as tk
def create_box(root, x1, y1, x2, y2, fill_color):
    canvas = tk.Canvas(root, width=300, height=200, bg="white")
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")
    return canvas
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Simple Canvas Box")
    box_x1 = 50
    box_y1 = 50
    box_x2 = 250
    box_y2 = 150
    fill_color = "lightblue"
    canvas_widget = create_box(root, box_x1, box_y1, box_x2, box_y2, fill_color)
    canvas_widget.pack(pady=20)
    root.mainloop()