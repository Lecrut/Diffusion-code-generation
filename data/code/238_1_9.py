import math
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
        print(f"Drawing Box at ({x1}, {y1}) with dimensions {self.width}x{self.height}")
def main():
    box = Box(x=10, y=20, width=50, height=30)
    canvas_width = 100
    canvas_height = 100
    print("--- Drawing Box ---")
    box.draw(canvas_width, canvas_height)
if __name__ == '__main__':
    main()