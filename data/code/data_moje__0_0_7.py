def convert_length(length: float, unit: str) -> float:
    unit = unit.lower()
    if unit == 'm':
        return length
    if unit == 'cm':
        return length / 100.0
    if unit == 'mm':
        return length / 1000.0
    if unit == 'km':
        return length * 1000.0
    if unit == 'in':
        return length * 0.0254
    if unit == 'ft':
        return length * 0.3048
    if unit == 'yd':
        return length * 0.9144
    if unit == 'mi':
        return length * 1609.344
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(convert_length(100, 'm'))
    print(convert_length(1, 'km'))
    print(convert_length(1, 'ft'))