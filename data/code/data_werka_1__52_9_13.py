from typing import Union

class GeometryCalculator:
    @staticmethod
    def calculate_area(length: float, width: float) -> float:
        return length * width

if __name__ == '__main__':
    length_rect: float = 12.0
    width_rect: float = 8.0
    area_rect: float = GeometryCalculator.calculate_area(length_rect, width_rect)
    print(area_rect)