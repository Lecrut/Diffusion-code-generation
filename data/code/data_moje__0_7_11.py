def convert_length(value: float, unit: str) -> float:
    conversions = {'m': 1.0, 'ft': 3.28084}
    if unit == 'm':
        return value
    if unit == 'ft':
        return value / conversions['ft']
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(convert_length(100.0, 'm'))
    print(convert_length(328.084, 'ft'))
    print(convert_length(10.0, 'ft'))