def convert_to_kilograms(measurements):
    results = []
    for measurement in measurements:
        try:
            if isinstance(measurement, dict) and 'value' in measurement and 'unit' in measurement:
                value = measurement['value']
                unit = measurement['unit'].lower().strip()
                if unit in ('kg', 'kilogram', 'kilograms'):
                    results.append(float(value))
                elif unit in ('g', 'gram', 'grams'):
                    results.append(float(value) / 1000.0)
                elif unit in ('lb', 'lbs', 'pound', 'pounds'):
                    results.append(float(value) * 0.45359237)
                elif unit in ('oz', 'ounce', 'ounces'):
                    results.append(float(value) * 0.0283495231)
                elif unit in ('mg', 'milligram', 'milligrams'):
                    results.append(float(value) / 1000000.0)
                else:
                    results.append(f"Error: Unknown unit '{unit}'")
            else:
                raise ValueError("Invalid measurement format")
        except (ValueError, TypeError, KeyError):
            results.append(f"Error: Could not parse {measurement}")
    return results

if __name__ == '__main__':
    sample_data = [
        {'value': 100, 'unit': 'g'},
        {'value': 2, 'unit': 'lbs'},
        {'value': 500, 'unit': 'kg'},
        {'value': 16, 'unit': 'oz'},
        {'value': 2000, 'unit': 'mg'},
        {'value': 10, 'unit': 'stone'},
        "invalid_string",
        {'value': 'not_a_number', 'unit': 'kg'},
        {'value': 10}
    ]
    converted_results = convert_to_kilograms(sample_data)
    print(converted_results)