def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    units = {
        "meter": 1.0,
        "m": 1.0,
        "kilometer": 1000.0,
        "km": 1000.0,
        "centimeter": 0.01,
        "cm": 0.01,
        "millimeter": 0.001,
        "mm": 0.001,
        "inch": 0.0254,
        "in": 0.0254,
        "foot": 0.3048,
        "ft": 0.3048,
        "yard": 0.9144,
        "yd": 0.9144,
        "mile": 1609.344,
        "mi": 1609.344,
        "nautical mile": 1852.0,
        "nmi": 1852.0,
    }

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in units:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    value_in_meters = value * units[from_unit]
    return value_in_meters / units[to_unit]

if __name__ == "__main__":
    result = convert_length(100, "cm", "m")
    print(result)
    result = convert_length(1, "mile", "kilometer")
    print(result)
    result = convert_length(12, "in", "cm")
    print(result)