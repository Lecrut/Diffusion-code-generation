class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = {'side1': side1, 'side2': side2, 'side3': side3}
        self._validate_sides()

    def _validate_sides(self):
        for side in self.sides.values():
            if not isinstance(side, (int, float)) or side <= 0:
                raise ValueError("All sides must be positive numbers.")
        
        side_values = sorted(self.sides.values())
        if side_values[0] + side_values[1] <= side_values[2]:
            raise ValueError("The given sides do not form a valid triangle.")

    def perimeter(self):
        return sum(self.sides.values())

if __name__ == '__main__':
    try:
        triangle = Triangle(10, 6, 8)
        print(triangle.perimeter())
        print(f'Side 1: {triangle.sides["side1"]}, Side 2: {triangle.sides["side2"]}, Side 3: {triangle.sides["side3"]}')
    except ValueError as e:
        print(e)