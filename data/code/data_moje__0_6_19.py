def convert_length(value, from_unit, to_unit):
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344,
    }
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in units:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in units:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    meters = value * units[from_unit_lower]
    return meters / units[to_unit_lower]

if __name__ == '__main__':
    result1 = convert_length(1, "m", "ft")
    print(result1)
    result2 = convert_length(100, "cm", "in")
    print(result2)
    result3 = convert_length(1, "mi", "km")
    print(result3)
    result4 = convert_length(5.5, "yd", "m")
    print(result4)