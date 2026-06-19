class Triangle:
    def __init__(self, sides):
        self.sides = sides

    @staticmethod
    def validate_sides(sides):
        if any(side <= 0 for side in sides):
            raise ValueError("Side lengths must be positive.")
        a, b, c = sides
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The given side lengths do not form a valid triangle.")

    @property
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        t1 = Triangle((3, 4, 5))
        print(t1.perimeter)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        t2 = Triangle((1, 2, 10))
        print(t2.perimeter)
    except ValueError as e:
        print(f"Error: {e}")