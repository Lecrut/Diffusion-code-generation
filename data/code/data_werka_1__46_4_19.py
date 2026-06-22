class Triangle:
    MIN_SIDE_LENGTH = 1

    def __init__(self, side_a, side_b, side_c):
        if not all(isinstance(side, int) and side >= self.MIN_SIDE_LENGTH for side in (side_a, side_b, side_c)):
            raise ValueError("All sides must be positive integers.")
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("Invalid triangle sides.")
        self.sides = [side_a, side_b, side_c]

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)