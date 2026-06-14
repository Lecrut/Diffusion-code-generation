import math
class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, canvas_x, canvas_y):
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        print(f"Drawing Box at ({x1}, {y1}) with dimensions ({self.width}, {self.height}) onto canvas starting at ({canvas_x}, {canvas_y}):")
        print(f"  Top-Left: ({x1}, {y1})")
        print(f"  Bottom-Right: ({x2}, {y2})")
if __name__ == '__main__':
    my_box = Box(10, 20, 5, 3)
    canvas_x = 0
    canvas_y = 0
    my_box.draw(canvas_x, canvas_y)