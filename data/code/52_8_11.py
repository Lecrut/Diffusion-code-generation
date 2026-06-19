from typing import Union

class AreaCalculator:
    def square(self, side_length: float) -> float:
        return side_length * side_length

    def rectangle(self, length: float, width: float) -> float:
        return length * width

    def circle(self, radius: float) -> float:
        import math
        return math.pi * radius * radius

    def triangle(self, base: float, height: float) -> float:
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = AreaCalculator()
    square_area = calculator.square(4.0)
    rectangle_area = calculator.rectangle(5.0, 3.0)
    circle_area = calculator.circle(7.0)
    triangle_area = calculator.triangle(6.0, 4.0)
    print(f"Square Area: {square_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area:.2f}")
    print(f"Triangle Area: {triangle_area}")