class SimpleBox:
    def __init__(self):
        pass
    def draw(self, canvas, x, y, width, height):
        for i in range(y, y + height):
            for j in range(x, x + width):
                canvas[i][j] = '*'
if __name__ == '__main__':
    canvas_size = 20
    test_canvas = [[' ' for _ in range(canvas_size)] for _ in range(canvas_size)]
    box = SimpleBox()
    x = 5
    y = 5
    width = 10
    height = 8
    box.draw(test_canvas, x, y, width, height)
    for row in test_canvas:
        print("".join(row))