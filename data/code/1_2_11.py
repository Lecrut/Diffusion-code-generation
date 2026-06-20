def convert_to_kilograms(measurements):
    conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'lb': 0.453592,
        'lbs': 0.453592,
        'oz': 0.0283495,
        'ton': 907.185,
        'tons': 907.185,
        'metric_ton': 1000.0,
        'mt': 1000.0,
        'stone': 6.35029,
    }
    
    results = []
    
    for measurement in measurements:
        try:
            if isinstance(measurement, (int, float)):
                results.append(float(measurement))
            elif isinstance(measurement, str):
                parts = measurement.strip().split()
                if len(parts) != 2:
                    results.append(None)
                    continue
                value_str, unit_str = parts
                value = float(value_str)
                unit_lower = unit_str.lower()
                if unit_lower in conversion_factors:
                    converted = value * conversion_factors[unit_lower]
                    results.append(converted)
                else:
                    results.append(None)
            elif isinstance(measurement, dict):
                if 'value' in measurement and 'unit' in measurement:
                    value = float(measurement['value'])
                    unit_lower = str(measurement['unit']).lower()
                    if unit_lower in conversion_factors:
                        converted = value * conversion_factors[unit_lower]
                        results.append(converted)
                    else:
                        results.append(None)
                else:
                    results.append(None)
            else:
                results.append(None)
        except (ValueError, TypeError, KeyError):
            results.append(None)
    
    return results

if __name__ == '__main__':
    sample_measurements = [
        5.0,
        "10 kg",
        "100 g",
        "2.5 lbs",
        "0.5 oz",
        {"value": 1, "unit": "ton"},
        "invalid",
        "50 metric_ton",
        -3.0,
        {"value": 10, "unit": "stone"},
        "123",
        "abc kg"
    ]
    converted_values = convert_to_kilograms(sample_measurements)
    print(converted_values)