class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    shapes = {
        'triangle': Triangle(3, 4),
        'trapezoid': Trapezoid(5, 7, 8)
    }

    total_area = sum(shape.area() for shape in shapes.values())
    print(total_area)