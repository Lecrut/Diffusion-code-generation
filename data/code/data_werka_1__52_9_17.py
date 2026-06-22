from typing import Tuple

class Geometry:
    @staticmethod
    def calculate_area(length: float, width: float) -> float:
        return length * width

if __name__ == '__main__':
    sample_values: Tuple[float, float] = (10.0, 5.0)
    area_result = Geometry.calculate_area(*sample_values)
    print(area_result)