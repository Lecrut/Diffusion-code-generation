def normalize_to_meters(distance, unit):
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance must be a number")
    if not isinstance(unit, str):
        raise TypeError("Unit must be a string")

    unit = unit.lower().strip()
    factors = {
        "m": 1.0,
        "meter": 1.0,
        "meters": 1.0,
        "km": 1000.0,
        "kilometer": 1000.0,
        "kilometers": 1000.0,
        "cm": 0.01,
        "centimeter": 0.01,
        "centimeters": 0.01,
        "mm": 0.001,
        "millimeter": 0.001,
        "millimeters": 0.001,
        "mi": 1609.344,
        "mile": 1609.344,
        "miles": 1609.344,
        "ft": 0.3048,
        "foot": 0.3048,
        "feet": 0.3048,
        "in": 0.0254,
        "inch": 0.0254,
        "inches": 0.0254,
        "yd": 0.9144,
        "yard": 0.9144,
        "yards": 0.9144,
        "nmi": 1852.0,
        "nautical mile": 1852.0,
        "nautical miles": 1852.0
    }

    if unit not in factors:
        raise ValueError(f"Unsupported unit: {unit}")

    return distance * factors[unit]

if __name__ == '__main__':
    samples = [
        (100, "meters"),
        (5.5, "km"),
        (3.2, "miles"),
        (12, "inches"),
        (1, "nautical mile"),
        (200, "cm")
    ]

    for dist, unit in samples:
        result = normalize_to_meters(dist, unit)
        print(result)