from typing import Dict, Tuple

UNIT_FACTORS: Dict[str, float] = {
    "px": 1.0,
    "cm": 1.0,
    "m": 1.0,
    "mm": 0.1,
}

def calculate_triangle_area(base: float, height: float, unit: str = "px") -> float:
    factor = UNIT_FACTORS.get(unit, 1.0)
    if base < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return 0.5 * (base * factor) * (height * factor)

if __name__ == '__main__':
    test_base = 8.0
    test_height = 4.5
    result = calculate_triangle_area(test_base, test_height)
    print(result)