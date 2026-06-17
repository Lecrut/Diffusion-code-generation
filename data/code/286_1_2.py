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
                result[key] = value * conversion_factors[unit]
            else:
                result[key] = value                                 
        except TypeError:
            result[key] = None
    return result
if __name__ == '__main__':
    sample_data = {
        "length_cm": 150.5,
        "distance_km": 2.5,
        "width_mm": 500,
        "area_m2": 10.0,
        "unknown_unit": 99
    }
    converted_data = convert_lengths(sample_data)
    print(converted_data)