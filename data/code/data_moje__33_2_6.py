class Triangle:
    def __init__(self, base, height):
        if base < 0 or height < 0:
            raise ValueError("Base and height must be non-negative")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = Triangle(10, 5)
    print(triangle.calculate_area())