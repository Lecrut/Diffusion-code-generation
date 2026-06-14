class SimpleBox:
    def __init__(self):
        pass
    def draw(self, canvas, x, y, width, height):
        for i in range(y, y + height):
            for j in range(x, x + width):
                canvas[i][j] = '*'
if __name__ == '__main__':
    canvas_size = 20
    canvas = [[' ' for _ in range(canvas_size)] for _ in range(canvas_size)]
    box = SimpleBox()
    x1, y1, w1, h1 = 5, 5, 10, 10
    box.draw(canvas, x1, y1, w1, h1)
    for row in canvas:
        print("".join(row))