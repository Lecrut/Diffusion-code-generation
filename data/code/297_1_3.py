def convert_length(length, source_unit):
    conversions = {
        "m": 1.0,
        "cm": 0.01,
        "km": 1000.0,
        "mm": 0.001,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34,
    }
    if source_unit not in conversions:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    results = {}
    for target_unit, factor in conversions.items():
        if target_unit == source_unit:
            results[target_unit] = length
        else:
            results[target_unit] = length * factor
    return results
if __name__ == '__main__':
    length_value = 10
    source_unit = "m"
    converted_values = convert_length(length_value, source_unit)
    print(f"Length: {length_value} {source_unit}")
    for unit, value in converted_values.items():
        print(f"{unit}: {value:.4f}")
    length_value_2 = 100
    source_unit_2 = "km"
    converted_values_2 = convert_length(length_value_2, source_unit_2)
    print(f"\nLength: {length_value_2} {source_unit_2}")
    for unit, value in converted_values_2.items():
        print(f"{unit}: {value:.4f}")
    try:
        convert_length(10, "lightyear")
    except ValueError as e:
        print(f"\nError caught: {e}")