class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if any(side <= 0 for side in self.sides):
            raise ValueError("All sides of the triangle must be positive.")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        valid_triangle = Triangle(3, 4, 5)
        print(valid_triangle.perimeter())
    except ValueError as e:
        print(f"Error: {e}")

    try:
        invalid_triangle_zero = Triangle(3, 4, 0)
        print(invalid_triangle_zero.perimeter())
    except ValueError as e:
        print(f"Error: {e}")

    try:
        invalid_triangle_negative = Triangle(3, -4, 5)
        print(invalid_triangle_negative.perimeter())
    except ValueError as e:
        print(f"Error: {e}")