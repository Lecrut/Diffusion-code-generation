import math
import sys
from typing import Union

Number = Union[int, float]

class EllipseCalculator:
    def __init__(self, semi_major: Number, semi_minor: Number) -> None:
        self._semi_major = float(semi_major)
        self._semi_minor = float(semi_minor)
        if self._semi_major <= 0:
            raise ValueError("Semi-major axis must be positive")
        if self._semi_minor <= 0:
            raise ValueError("Semi-minor axis must be positive")

    @property
    def semi_major(self) -> float:
        return self._semi_major

    @property
    def semi_minor(self) -> float:
        return self._semi_minor

    def calculate_area(self) -> float:
        return self._semi_major * self._semi_minor * math.pi

def calculate_ellipse_area(semi_major: Number, semi_minor: Number) -> float:
    semi_major_val = float(semi_major)
    semi_minor_val = float(semi_minor)
    if semi_major_val <= 0:
        raise ValueError("Semi-major axis must be positive")
    if semi_minor_val <= 0:
        raise ValueError("Semi-minor axis must be positive")
    return semi_major_val * semi_minor_val * math.pi

if __name__ == '__main__':
    sample_semi_major = 5.0
    sample_semi_minor = 3.0
    result = calculate_ellipse_area(sample_semi_major, sample_semi_minor)
    print(result)
    calculator = EllipseCalculator(sample_semi_major, sample_semi_minor)
    print(calculator.calculate_area())