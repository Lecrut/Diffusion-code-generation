class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = {'side1': side1, 'side2': side2, 'side3': side3}
        self._validate_sides()

    def _validate_sides(self):
        for side in self.sides.values():
            if not isinstance(side, (int, float)) or side <= 0:
                raise ValueError("All sides must be positive numbers.")
        
        a, b, c = sorted(self.sides.values())
        if a + b <= c:
            raise ValueError("The given sides do not form a valid triangle.")

    def perimeter(self):
        return sum(self.sides.values())

if __name__ == '__main__':
    try:
        triangle = Triangle(10, 6, 8)
        print(triangle.perimeter())
        for side_name, length in triangle.sides.items():
            print(f'{side_name}: {length}')
    except ValueError as e:
        print(e)