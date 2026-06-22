import math

UNIT_MULTIPLIERS = {
    "cm": 1.0,
    "mm": 0.1,
    "m": 100.0,
    "in": 2.54,
}

def _validate_and_normalize(radius: float, unit: str) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if unit not in UNIT_MULTIPLIERS:
        raise ValueError(f"Unsupported unit: {unit}")
    return radius * UNIT_MULTIPLIERS[unit]

def calculate_circle_area(radius: float, unit: str = "cm") -> float:
    normalized_radius = _validate_and_normalize(radius, unit)
    return math.pi * (normalized_radius ** 2)

if __name__ == '__main__':
    test_cases = [
        {"radius": 10.0, "unit": "cm"},
        {"radius": 5.0, "unit": "m"},
        {"radius": 2.0, "unit": "mm"},
    ]

    for case in test_cases:
        val = case["radius"]
        u = case["unit"]
        area = calculate_circle_area(val, u)
        print(f"Radius: {val} {u}, Area: {area}")