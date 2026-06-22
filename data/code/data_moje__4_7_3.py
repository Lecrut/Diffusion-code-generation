UNIT_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}

def normalize_distance(value: float, unit: str) -> float:
    unit_lower = unit.lower()
    if unit_lower not in UNIT_TO_METERS:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * UNIT_TO_METERS[unit_lower]

if __name__ == '__main__':
    print(normalize_distance(1.5, "km"))
    print(normalize_distance(12, "in"))