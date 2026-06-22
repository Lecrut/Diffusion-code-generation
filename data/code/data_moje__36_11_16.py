from __future__ import annotations

import math

BASE_FACTOR: float = 0.5

def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
    return BASE_FACTOR * (base1 + base2) * height

if __name__ == '__main__':
    first_base: float = 12.0
    second_base: float = 8.0
    altitude: float = 5.0
    result: float = calculate_trapezoid_area(first_base, second_base, altitude)
    print(result)