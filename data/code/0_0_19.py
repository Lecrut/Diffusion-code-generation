def convert_length(value: float, unit: str) -> float:
    factors = {
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    if unit not in factors:
        raise ValueError(f"Unsupported unit: {unit}")
    meters = value * factors[unit]
    return meters

if __name__ == '__main__':
    result_m = convert_length(1, 'm')
    print(result_m)
    result_ft = convert_length(1, 'ft')
    print(result_ft)