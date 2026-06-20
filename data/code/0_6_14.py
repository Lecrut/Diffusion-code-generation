def convert_length(value, from_unit, to_unit):
    factors = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
        'nm': 1e-9,
    }

    if from_unit not in factors:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in factors:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    value_in_meters = value * factors[from_unit]
    return value_in_meters / factors[to_unit]

if __name__ == '__main__':
    result = convert_length(1, 'km', 'm')
    print(result)