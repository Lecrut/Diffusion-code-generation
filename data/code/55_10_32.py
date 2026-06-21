class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    @property
    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    triangle_sides = {'triangle1': (3, 4, 5), 'triangle2': (6, 8, 10), 'triangle3': (7, 9, 12)}
    for name, sides in triangle_sides.items():
        triangle = Triangle(*sides)
        print(f'{name} perimeter: {triangle.perimeter}')