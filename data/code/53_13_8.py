from typing import Union

class ShapeCalculator:
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

    def calculate_perimeter(self) -> float:
        return 4 * self.side_length

def main():
    try:
        side_length = 5.0
        calculator = ShapeCalculator(side_length)
        area = calculator.calculate_area()
        perimeter = calculator.calculate_perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()