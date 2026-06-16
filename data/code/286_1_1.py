def convert_lengths(measurements):
    conversion_factors = {
        'm': 1.0,
        'cm': 0.01,
        'km': 1000.0,
        'mm': 0.001
    }
    result = {}
    for key, value in measurements.items():
        try:
            unit = key.lower()
            if unit in conversion_factors:
                converted_value = value * conversion_factors[unit]
                result[key] = converted_value
            else:
                result[key] = None
        except TypeError:
            result[key] = None
    return result
if __name__ == '__main__':
    sample_data = {
        "length1": 50.0,
        "length2": 250.5,
        "area3": 10000,
        "weight4": 5.5,
        "length5": 1.23,
        "invalid_key": "not_a_number",
        "length6": 2.5,
        "length7": 100
    }
    converted = convert_lengths(sample_data)
    print(converted)