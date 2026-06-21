from typing import Union

class Triangle:
    BASE = 10.0
    HEIGHT = 5.0

    @staticmethod
    def area(base: float, height: float) -> float:
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        return 0.5 * base * height

if __name__ == '__main__':
    try:
        triangle = Triangle()
        area_result = Triangle.area(triangle.BASE, triangle.HEIGHT)
        print(area_result)
    except ValueError as e:
        print(e)