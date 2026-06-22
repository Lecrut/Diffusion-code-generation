import math
from typing import List, Tuple, Union

Number = Union[int, float]

class EllipseCalculator:
    def __init__(self, tolerance: Number = 1e-9) -> None:
        if not isinstance(tolerance, (int, float)) or tolerance < 0:
            raise TypeError("Tolerance must be a non-negative number")
        self.tolerance = tolerance

    def validate_axes(self, major: Number, minor: Number) -> None:
        if not isinstance(major, (int, float)) or not isinstance(minor, (int, float)):
            raise TypeError("Both major and minor axes must be numbers")
        if major <= 0 or minor <= 0:
            raise ValueError("Both axes must be strictly positive")

    def calculate_area(self, major: Number, minor: Number) -> float:
        self.validate_axes(major, minor)
        return math.pi * major * minor

    def calculate_areas_batch(self, pairs: List[Tuple[Number, Number]]) -> List[float]:
        if not isinstance(pairs, list):
            raise TypeError("Input must be a list of tuples")
        areas = []
        for item in pairs:
            if not isinstance(item, (tuple, list)) or len(item) != 2:
                raise TypeError("Each item in the list must be a pair of numbers")
            areas.append(self.calculate_area(item[0], item[1]))
        return areas

if __name__ == '__main__':
    calculator = EllipseCalculator()
    sample_pairs = [(10, 5), (7.5, 3.2), (20, 20), (1.5, 4.5)]
    results = calculator.calculate_areas_batch(sample_pairs)
    for area in results:
        print(area)