class AsciiTriangle:
    def __init__(self, height):
        self.height = height

    def draw(self):
        for i in range(1, self.height + 1):
            spaces = " " * (self.height - i)
            stars = "* " * i
            print(spaces + stars.strip())

if __name__ == '__main__':
    triangle = AsciiTriangle(5)
    triangle.draw()