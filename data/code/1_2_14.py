def convert_to_kilograms(measurements):
    conversion_factors = {
        'kg': 1.0,
        'kilogram': 1.0,
        'kilograms': 1.0,
        'g': 0.001,
        'gram': 0.001,
        'grams': 0.001,
        'mg': 0.000001,
        'milligram': 0.000001,
        'milligrams': 0.000001,
        'mg': 0.000001,
        'lb': 0.453592,
        'lbs': 0.453592,
        'pound': 0.453592,
        'pounds': 0.453592,
        'oz': 0.0283495,
        'ounce': 0.0283495,
        'ounces': 0.0283495,
        'ton': 907.185,
        'tons': 907.185,
        'stone': 6.35029,
        'stones': 6.35029
    }

    results = []

    for measurement in measurements:
        try:
            if not isinstance(measurement, (list, tuple)) or len(measurement) != 2:
                results.append(None)
                continue

            value, unit = measurement

            if not isinstance(value, (int, float)):
                results.append(None)
                continue

            if value < 0:
                results.append(None)
                continue

            if not isinstance(unit, str):
                results.append(None)
                continue

            unit_lower = unit.strip().lower()

            if unit_lower not in conversion_factors:
                results.append(None)
                continue

            converted = value * conversion_factors[unit_lower]
            results.append(converted)

        except Exception:
            results.append(None)

    return results

if __name__ == '__main__':
    sample_measurements = [
        [10, 'kg'],
        [100, 'g'],
        [2, 'lb'],
        [16, 'oz'],
        [0.5, 'ton'],
        [14, 'stone'],
        [500, 'mg'],
        [-5, 'kg'],
        ['abc', 'kg'],
        [10, 'invalid_unit'],
        [10],
        None,
        [10, 'kilograms']
    ]

    result = convert_to_kilograms(sample_measurements)
    print(result)