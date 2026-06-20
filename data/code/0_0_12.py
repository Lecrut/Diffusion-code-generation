def convert_length(length: float, unit: str) -> float:
    units_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    if unit not in units_to_meters:
        raise ValueError(f"Unsupported unit: {unit}")
    meters = length * units_to_meters[unit]
    return meters

if __name__ == '__main__':
    sample_length = 100
    sample_unit = 'ft'
    converted = convert_length(sample_length, sample_unit)
    print(converted)