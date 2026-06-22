import math
from typing import Union

Number = Union[int, float]

class Ellipse:
    def __init__(self, semi_major: Number, semi_minor: Number) -> None:
        if not isinstance(semi_major, (int, float)) or not isinstance(semi_minor, (int, float)):
            raise TypeError("Semi-major and semi-minor axes must be numeric types.")
        if semi_major <= 0 or semi_minor <= 0:
            raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
        self.semi_major = float(semi_major)
        self.semi_minor = float(semi_minor)

    def area(self) -> float:
        return self.semi_major * self.semi_minor * math.pi

def calculate_ellipse_area(semi_major: Number, semi_minor: Number) -> float:
    if not isinstance(semi_major, (int, float)) or not isinstance(semi_minor, (int, float)):
        raise TypeError("Semi-major and semi-minor axes must be numeric types.")
    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("Semi-major and semi-minor axes must be positive numbers.")
    return float(semi_major) * float(semi_minor) * math.pi

if __name__ == '__main__':
    sample_semi_major = 5.0
    sample_semi_minor = 3.0
    direct_area = calculate_ellipse_area(sample_semi_major, sample_semi_minor)
    print(direct_area)
    ellipse_instance = Ellipse(sample_semi_major, sample_semi_minor)
    print(ellipse_instance.area())