class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self._sum_sides()

    def _sum_sides(self) -> float:
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    DEFAULT_SIDE1 = 7.0
    DEFAULT_SIDE2 = 9.0
    DEFAULT_SIDE3 = 12.0
    triangle = Triangle(DEFAULT_SIDE1, DEFAULT_SIDE2, DEFAULT_SIDE3)
    print(triangle.perimeter())