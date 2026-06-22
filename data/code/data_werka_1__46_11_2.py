class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle = Triangle(3.0, 4.0, 5.0)
    print(triangle.perimeter())