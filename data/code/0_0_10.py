def convert_length(length: float, unit: str) -> float:
    unit = unit.lower()
    if unit == 'm':
        return length
    elif unit == 'ft':
        return length * 3.28084
    elif unit == 'km':
        return length * 0.001
    elif unit == 'mi':
        return length * 0.000621371
    elif unit == 'cm':
        return length * 100
    elif unit == 'in':
        return length * 39.3701
    elif unit == 'yd':
        return length * 1.09361
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    print(convert_length(1, 'm'))
    print(convert_length(1, 'ft'))
    print(convert_length(100, 'm'))
    print(convert_length(5, 'km'))
    print(convert_length(10, 'mi'))
    print(convert_length(1, 'cm'))
    print(convert_length(1, 'in'))
    print(convert_length(1, 'yd'))