from typing import Union

class GeometricShape:
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

    def calculate_perimeter(self) -> float:
        return 4 * self.side_length

if __name__ == '__main__':
    try:
        side_length = 5.0
        square = GeometricShape(side_length)
        area = square.calculate_area()
        perimeter = square.calculate_perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(e)