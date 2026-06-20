def convert_length(length: float, unit: str) -> float:
    unit = unit.lower().strip()
    if unit == 'm':
        return length
    elif unit == 'ft':
        return length * 0.3048
    elif unit == 'in':
        return length * 0.0254
    elif unit == 'cm':
        return length * 0.01
    elif unit == 'km':
        return length * 1000.0
    elif unit == 'mi':
        return length * 1609.344
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(convert_length(10, 'ft'))
    print(convert_length(1, 'mi'))
    print(convert_length(100, 'cm'))
    print(convert_length(5, 'm'))
    print(convert_length(12, 'in'))
    print(convert_length(5.5, 'km'))