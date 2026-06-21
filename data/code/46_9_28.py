class Triangle:
    MIN_SIDE_LENGTH = 1.0

    def __init__(self, side1: float, side2: float, side3: float):
        if not (side1 >= self.MIN_SIDE_LENGTH and side2 >= self.MIN_SIDE_LENGTH and side3 >= self.MIN_SIDE_LENGTH):
            raise ValueError("Side lengths must be greater than or equal to the minimum side length.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return Triangle._sum_sides(self.side1, self.side2, self.side3)

    @staticmethod
    def _sum_sides(a: float, b: float, c: float) -> float:
        return a + b + c

if __name__ == '__main__':
    side_a = 7.0
    side_b = 9.0
    side_c = 12.0
    triangle = Triangle(side_a, side_b, side_c)
    print(triangle.perimeter())