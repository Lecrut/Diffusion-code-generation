class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, canvas_width, canvas_height):
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        if x1 < 0 or y1 < 0 or x2 > canvas_width or y2 > canvas_height:
            return
        print(f"Drawing box at ({x1}, {y1}) with dimensions {self.width}x{self.height} on canvas {canvas_width}x{canvas_height}")
if __name__ == '__main__':
    box1 = Box(10, 20, 50, 30)
    print("--- Drawing Box 1 ---")
    box1.draw(100, 100)
    box2 = Box(50, 50, 20, 40)
    print("\n--- Drawing Box 2 ---")
    box2.draw(100, 100)