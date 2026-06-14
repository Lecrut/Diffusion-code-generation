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
        print(f"Drawing box at ({x1}, {y1}) with dimensions {self.width}x{self.height} onto canvas starting at ({canvas_x}, {canvas_y}).")
        print(f"  Top-left corner of box: ({x1}, {y1})")
        print(f"  Bottom-right corner of box: ({x2}, {y2})")
if __name__ == '__main__':
    box1 = Box(10, 20, 50, 30)
    box2 = Box(100, 50, 20, 75)
    print("--- Drawing Box 1 ---")
    box1.draw(0, 0)
    print("\n--- Drawing Box 2 ---")
    box2.draw(50, 50)