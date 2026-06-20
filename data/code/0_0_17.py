def convert_length(value: float, unit: str) -> float:
    if unit == 'm':
        return value
    if unit == 'ft':
        return value * 0.3048
    if unit == 'cm':
        return value * 0.01
    if unit == 'in':
        return value * 0.0254
    if unit == 'km':
        return value * 1000
    if unit == 'mi':
        return value * 1609.34
    if unit == 'mm':
        return value * 0.001
    if unit == 'yd':
        return value * 0.9144
    return value

if __name__ == '__main__':
    print(convert_length(10, 'ft'))
    print(convert_length(1, 'm'))
    print(convert_length(5.5, 'km'))
    print(convert_length(12, 'in'))