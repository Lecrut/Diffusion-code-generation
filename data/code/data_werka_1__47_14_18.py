from typing import Tuple

class Triangle:
    BASE_MULTIPLIER: float = 0.5

    @staticmethod
    def calculate_area(base: float, height: float) -> float:
        return Triangle.BASE_MULTIPLIER * base * height

if __name__ == '__main__':
    dimensions: Tuple[float, float] = (20.0, 10.0)
    triangle = Triangle()
    area = triangle.calculate_area(*dimensions)
    print(area)