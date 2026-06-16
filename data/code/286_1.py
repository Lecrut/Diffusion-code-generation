def convert_lengths(measurements):
    converted = {}
    for key, value in measurements.items():
        unit = measurements[key].get('unit', 'm')
        try:
            if unit == 'm':
                converted[key] = float(value)
            elif unit == 'cm':
                converted[key] = float(value) / 100.0
            elif unit == 'km':
                converted[key] = float(value) * 1000.0
            else:
                converted[key] = float(value)
        except (ValueError, TypeError):
            converted[key] = None
    return converted
if __name__ == '__main__':
    sample_data = {
        "length_a": {"value": 150.5, "unit": "cm"},
        "length_b": {"value": 2.5, "unit": "km"},
        "length_c": {"value": 300, "unit": "m"},
        "invalid_length": {"value": "not_a_number", "unit": "m"},
        "length_d": {"value": 10.0, "unit": "ft"}
    }
    result = convert_lengths(sample_data)
    print(result)