class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = {'a': side1, 'b': side2, 'c': side3}
        self._validate_triangle()

    def _validate_triangle(self):
        for side in self.sides.values():
            if not isinstance(side, (int, float)) or side <= 0:
                raise ValueError("All sides must be positive numbers.")
        a, b, c = sorted(self.sides.values())
        if not (a + b > c):
            raise ValueError("The given sides do not form a valid triangle.")

    def perimeter(self):
        return sum(self.sides.values())

if __name__ == '__main__':
    try:
        triangle = Triangle(10, 12, 5)
        print(triangle.perimeter())
        for key, value in triangle.sides.items():
            print(f'Side {key}: {value}')
    except ValueError as e:
        print(e)