class Shape:
    def __init__(self, area_formula, dimensions):
        self.area_formula = area_formula
        self.dimensions = dimensions

    def calculate_area(self):
        return self.area_formula(self.dimensions)

class Rhombus(Shape):
    def __init__(self, d1, d2):
        super().__init__(area_rhombus, [d1, d2])

class Square(Shape):
    def __init__(self, side):
        super().__init__(area_square, [side])

def area_rhombus(d1, d2):
    return 0.5 * d1 * d2

def area_square(side):
    return side ** 2

if __name__ == '__main__':
    rhombus = Rhombus(10, 8)
    square = Square(6)

    print(f"Rhombus Area: {rhombus.calculate_area()}")
    print(f"Square Area: {square.calculate_area()}")