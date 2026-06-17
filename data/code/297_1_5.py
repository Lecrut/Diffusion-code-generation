def convert_length(length, source_unit):
    conversions = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 100.0,
        "millimeter": 10.0,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
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
    sample_length = 10
    source_unit = "meter"
    converted_values = convert_length(sample_length, source_unit)
    print(f"Length: {sample_length} {source_unit}")
    for unit, value in converted_values.items():
        print(f"{unit}: {value:.4f}")
    sample_length_2 = 100
    source_unit_2 = "kilometer"
    converted_values_2 = convert_length(sample_length_2, source_unit_2)
    print(f"\nLength: {sample_length_2} {source_unit_2}")
    for unit, value in converted_values_2.items():
        print(f"{unit}: {value:.4f}")