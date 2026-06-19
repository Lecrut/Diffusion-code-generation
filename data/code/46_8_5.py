class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self._is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def _is_valid_triangle(self):
        a, b, c = sorted(self.sides)
        return a + b > c

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        sample_triangle = Triangle(9, 12, 15)
        print(sample_triangle.perimeter())
    except ValueError as e:
        print(e)