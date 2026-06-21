class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = {'side1': side1, 'side2': side2, 'side3': side3}

    def perimeter(self):
        return sum(self.sides.values())

if __name__ == '__main__':
    triangle_sides = {'side1': 6, 'side2': 8, 'side3': 10}
    triangle = Triangle(**triangle_sides)
    print(triangle.perimeter())