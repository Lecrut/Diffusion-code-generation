def convert_length(value: float, unit: str) -> float:
    unit = unit.lower()
    meters = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'mi': 1609.344
    }
    if unit not in meters:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * meters[unit]

if __name__ == '__main__':
    print(convert_length(100, 'ft'))
    print(convert_length(5.5, 'm'))
    print(convert_length(1, 'km'))