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
        print(f"Drawing box at ({x1}, {y1}) with dimensions {self.width}x{self.height}")
        print(f"Coordinates: Top-Left=({x1}, {y1}), Bottom-Right=({x2}, {y2})")
if __name__ == '__main__':
    my_box = Box(10, 20, 50, 30)
    print("--- Testing Box Drawing ---")
    my_box.draw(0, 0)