import math
def convert_lengths(measurements):
    result = {}
    for key, value in measurements.items():
        unit = measurements[key]['unit']
        try:
            if unit == 'm':
                result[key] = float(value)
            elif unit == 'cm':
                result[key] = float(value) / 100.0
            elif unit == 'mm':
                result[key] = float(value) / 1000.0
            else:
                result[key] = float(value)                                                                    
        except (ValueError, TypeError):
            result[key] = None
    return result
if __name__ == '__main__':
    sample_data = {
        "length_a": {"value": 150.5, "unit": "cm"},
        "length_b": {"value": 2.5, "unit": "m"},
        "length_c": {"value": 500, "unit": "mm"},
        "length_d": {"value": 10, "unit": "km"},
        "invalid_length": {"value": "not_a_number", "unit": "m"},
        "valid_length": {"value": 3.14, "unit": "m"}
    }
    converted = convert_lengths(sample_data)
    print(converted)