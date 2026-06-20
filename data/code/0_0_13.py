def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    units_to_meters = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'km': 1000.0,
        'mi': 1609.344,
        'cm': 0.01,
        'mm': 0.001,
        'yd': 0.9144,
        'nm': 1e-9
    }
    if from_unit not in units_to_meters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    meters = value * units_to_meters[from_unit]
    return meters / units_to_meters[to_unit]

if __name__ == '__main__':
    print(convert_length(1.0, 'ft', 'm'))
    print(convert_length(100.0, 'm', 'ft'))
    print(convert_length(1.0, 'mi', 'km'))
    print(convert_length(12.0, 'in', 'cm'))