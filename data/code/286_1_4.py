def convert_lengths(measurements):
    conversion_factors = {
        'm': 1.0,
        'cm': 0.01,
        'km': 1000.0,
        'mm': 0.001
    }
    result = {}
    for key, value in measurements.items():
        if isinstance(value, (int, float)):
            unit = measurements[key]
            if unit in conversion_factors:
                result[key] = value * conversion_factors[unit]
            else:
                result[key] = None
        else:
            result[key] = None
    return result
if __name__ == '__main__':
    sample_data = {
        'length_cm': 150,
        'distance_km': 2.5,
        'width_mm': 500,
        'area_m2': 10.0,
        'invalid_value': "error",
        'length_m': 5.0
    }
    converted = convert_lengths(sample_data)
    print(converted)