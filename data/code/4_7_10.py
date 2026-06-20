def normalize_to_meters(value: float, unit: str) -> float:
    conversions = {
        "mm": 0.001,
        "cm": 0.01,
        "dm": 0.1,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
    }
    lower_unit = unit.lower()
    if lower_unit in conversions:
        return value * conversions[lower_unit]
    raise ValueError(f"Unknown unit: {unit}")

if __name__ == '__main__':
    result_mm = normalize_to_meters(1500, "mm")
    result_km = normalize_to_meters(2.5, "km")
    result_ft = normalize_to_meters(100, "ft")
    print(result_mm)
    print(result_km)
    print(result_ft)