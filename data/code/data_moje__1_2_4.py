def convert_to_kilograms(measurements):
    conversion_factors = {
        'g': 0.001,
        'kg': 1.0,
        'lb': 0.453592,
        'oz': 0.0283495,
        'ton': 907.185
    }
    results = []
    for measurement in measurements:
        try:
            if not isinstance(measurement, dict):
                raise ValueError("Each measurement must be a dictionary with 'value' and 'unit' keys")
            value = measurement['value']
            unit = measurement['unit'].lower().strip()
            if unit not in conversion_factors:
                raise ValueError(f"Unsupported unit: {unit}")
            converted_value = value * conversion_factors[unit]
            results.append(converted_value)
        except (KeyError, TypeError, ValueError) as e:
            results.append(None)
    return results

if __name__ == '__main__':
    sample_measurements = [
        {'value': 1000, 'unit': 'g'},
        {'value': 2.5, 'unit': 'kg'},
        {'value': 5, 'unit': 'lb'},
        {'value': 10, 'unit': 'oz'},
        {'value': 0.5, 'unit': 'ton'},
        {'value': 'invalid', 'unit': 'kg'},
        {'value': 10, 'unit': 'invalid_unit'}
    ]
    print(convert_to_kilograms(sample_measurements))