class SimpleBox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, canvas):
        for i in range(self.y, self.y + self.height):
            for j in range(self.x, self.x + self.width):
                canvas[i][j] = '*'
if __name__ == '__main__':
    canvas_width = 20
    canvas_height = 15
    canvas = [[' ' for _ in range(canvas_width)] for _ in range(canvas_height)]
    box = SimpleBox(5, 5, 10, 8)
    box.draw(canvas)
    for row in canvas:
        print("".join(row))