def convert_length(length, source_unit):
    conversion_factors = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
    }
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    results = {}
    for target_unit, factor in conversion_factors.items():
        if source_unit == target_unit:
            results[target_unit] = length
        else:
            value_in_meters = length * conversion_factors[source_unit]
            results[target_unit] = value_in_meters / conversion_factors[target_unit]
    return results
if __name__ == '__main__':
    sample_length = 10
    source_unit = "meter"
    converted_values = convert_length(sample_length, source_unit)
    print(f"Original Length: {sample_length} {source_unit}")
    print("Converted Values:")
    for unit, value in converted_values.items():
        print(f"{unit}: {value:.4f}")