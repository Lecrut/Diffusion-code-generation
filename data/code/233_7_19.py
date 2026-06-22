class RectangleFiller:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def fill(self):
        for _ in range(self.height):
            yield '*' * self.width

if __name__ == '__main__':
    filler = RectangleFiller(5, 3)
    for row in filler.fill():
        print(row)