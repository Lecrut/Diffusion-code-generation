import math
from typing import List, Tuple

def validate_positive_number(value: float, name: str) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def calculate_ellipse_area(major_axis: float, minor_axis: float) -> float:
    validate_positive_number(major_axis, "major_axis")
    validate_positive_number(minor_axis, "minor_axis")
    return math.pi * major_axis * minor_axis

def compute_ellipse_areas(pairs: List[Tuple[float, float]]) -> List[float]:
    areas = []
    for i, (major, minor) in enumerate(pairs):
        try:
            area = calculate_ellipse_area(major, minor)
            areas.append(area)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid pair at index {i}: {e}")
    return areas

if __name__ == "__main__":
    sample_pairs = [(10, 5), (7, 7), (15.5, 4.2), (2, 3)]
    results = compute_ellipse_areas(sample_pairs)
    for i, area in enumerate(results):
        print(f"Pair {i + 1} area: {area}")