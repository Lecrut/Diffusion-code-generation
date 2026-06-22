from typing import Union
from dataclasses import dataclass
from math import isclose

def compute_triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    half = 0.5
    raw_area = base * height
    final_area = half * raw_area
    return final_area

if __name__ == '__main__':
    sample_base = 12.5
    sample_height = 8.0
    area_result = compute_triangle_area(sample_base, sample_height)
    print(area_result)