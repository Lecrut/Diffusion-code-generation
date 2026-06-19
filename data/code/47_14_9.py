from typing import Tuple

class Triangle:
    BASE = 10.0
    HEIGHT = 5.0

    @staticmethod
    def calculate_area(base: float, height: float) -> float:
        return 0.5 * base * height

if __name__ == '__main__':
    area = Triangle.calculate_area(Triangle.BASE, Triangle.HEIGHT)
    print(area)