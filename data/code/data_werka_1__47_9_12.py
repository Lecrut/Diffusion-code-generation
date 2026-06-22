class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        if self.base <= 0 or self.height <= 0:
            return 0
        return (self.base * self.height) / 2

if __name__ == '__main__':
    triangle = Triangle(10, 5)
    print(triangle.area())