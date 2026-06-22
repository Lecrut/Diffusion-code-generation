class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle_sides = {
        'side1': 6,
        'side2': 8,
        'side3': 10
    }
    triangle = Triangle(**triangle_sides)
    perimeter = triangle.calculate_perimeter()
    print(perimeter)