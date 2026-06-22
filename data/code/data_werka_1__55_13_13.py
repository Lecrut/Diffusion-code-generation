class Triangle:
    def __init__(self, sides):
        self.sides = sides

    @staticmethod
    def validate_sides(sides):
        if any(side <= 0 for side in sides):
            raise ValueError("Side lengths must be positive.")
        a, b, c = sorted(sides)
        if a + b <= c:
            raise ValueError("The given side lengths do not form a valid triangle.")

    @property
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle((3, 4, 5))
        print(triangle.perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle = Triangle((1, 2, 10))
        print(triangle.perimeter)
    except ValueError as e:
        print(f"Error: {e}")