def convert_length(value, from_unit, to_unit):
    units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit")
    meters = value * units[from_unit]
    return meters / units[to_unit]

if __name__ == '__main__':
    print(convert_length(1, 'mi', 'km'))
    print(convert_length(100, 'cm', 'in'))
    print(convert_length(5, 'ft', 'm'))