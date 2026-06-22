class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle = Triangle(3.0, 4.0, 5.0)
    perimeter = triangle.calculate_perimeter()
    print(perimeter)

    another_triangle = Triangle(6.5, 7.8, 9.0)
    another_perimeter = another_triangle.calculate_perimeter()
    print(another_perimeter)