import json

def convert_to_kilograms(measurements):
    conversion_factors = {'kg': 1.0, 'g': 0.001, 'lb': 0.45359237, 'oz': 0.028349523125, 'ton': 907.18474, 't': 1000.0}
    results = []
    for measurement in measurements:
        try:
            if not isinstance(measurement, dict):
                raise TypeError('Each measurement must be a dictionary.')
            if 'value' not in measurement or 'unit' not in measurement:
                raise ValueError("Measurement must contain 'value' and 'unit'.")
            value = measurement['value']
            unit = measurement['unit']
            if not isinstance(value, (int, float)):
                raise TypeError('Value must be a number.')
            if not isinstance(unit, str):
                raise TypeError('Unit must be a string.')
            unit_lower = unit.lower().strip()
            if unit_lower not in conversion_factors:
                raise ValueError(f'Unknown unit: {unit}')
            kg_value = value * conversion_factors[unit_lower]
            results.append(kg_value)
        except Exception as e:
            print(f'Error processing measurement {measurement}: {e}')
            results.append(None)
    return results
if __name__ == '__main__':
    samples = [{'value': 1000, 'unit': 'g'}, {'value': 5, 'unit': 'lb'}, {'value': 10, 'unit': 'kg'}, {'value': -5, 'unit': 'kg'}, {'value': 'abc', 'unit': 'kg'}, {'value': 10, 'unit': 'invalid_unit'}]
    output = convert_to_kilograms(samples)
    print(output)