class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8)
        print(triangle.area)
    except ValueError as e:
        print(e)