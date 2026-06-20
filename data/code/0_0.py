def convert_length(length: float, unit: str) -> float:
    unit = unit.lower()
    if unit == 'm':
        return length
    elif unit == 'ft':
        return length * 0.3048
    elif unit == 'in':
        return length * 0.0254
    elif unit == 'km':
        return length * 1000.0
    elif unit == 'mi':
        return length * 1609.344
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(convert_length(1, 'm'))
    print(convert_length(1, 'ft'))
    print(convert_length(1, 'in'))
    print(convert_length(1, 'km'))
    print(convert_length(1, 'mi'))