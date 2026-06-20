def convert(length_value, from_unit, to_unit):
    factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.344,
    }

    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Unsupported unit provided")

    value_in_meters = length_value * factors[from_unit]
    result = value_in_meters / factors[to_unit]
    return result

if __name__ == '__main__':
    result = convert(1, 'kilometers', 'meters')
    print(result)