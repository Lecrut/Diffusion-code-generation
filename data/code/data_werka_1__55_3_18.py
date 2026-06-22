class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def calculate_perimeter(side1: float, side2: float, side3: float) -> float:
        return side1 + side2 + side3

if __name__ == '__main__':
    triangle = Triangle(3.5, 4.2, 5.1)
    perimeter = Triangle.calculate_perimeter(triangle.side1, triangle.side2, triangle.side3)
    print(perimeter)