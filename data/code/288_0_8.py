def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
scale_conversions = {'C': celsius_to_fahrenheit, 'F': fahrenheit_to_celsius}

def convert_temperature(value, scale_from, scale_to):
    if scale_from not in scale_conversions or scale_to not in scale_conversions:
        raise ValueError('Invalid temperature scale')
    converter = scale_conversions[scale_from]
    converted_value = converter(value)
    return converted_value
if __name__ == '__main__':
    print(convert_temperature(0, 'C', 'F'))
    print(convert_temperature(100, 'C', 'F'))
    print(convert_temperature(32, 'F', 'C'))
    print(convert_temperature(212, 'F', 'C'))