import math
from typing import List, Tuple, Union

Number = Union[int, float]

def validate_axis(value: Number, name: str) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")

def calculate_ellipse_areas(pairs: List[Tuple[Number, Number]]) -> List[float]:
    results = []
    for major, minor in pairs:
        validate_axis(major, "Major axis")
        validate_axis(minor, "Minor axis")
        area = math.pi * major * minor
        results.append(area)
    return results

if __name__ == "__main__":
    sample_data = [
        (10, 5),
        (14, 7.5),
        (3, 3)
    ]
    areas = calculate_ellipse_areas(sample_data)
    for index, area in enumerate(areas):
        print(f"Pair {index + 1}: {area}")