def normalize_to_meters(value, unit):
    conversion_factors = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
        "nmi": 1852.0
    }
    normalized_unit = unit.lower()
    if normalized_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * conversion_factors[normalized_unit]

if __name__ == '__main__':
    sample_values = [
        (100, "cm"),
        (5, "km"),
        (1, "mi"),
        (3, "ft"),
        (10, "in")
    ]
    for value, unit in sample_values:
        result = normalize_to_meters(value, unit)
        print(f"{value} {unit} = {result} m")