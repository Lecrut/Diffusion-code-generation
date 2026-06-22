conversion_factors = {'CtoF': (9, 5, 32), 'FtoC': (5, 9, -160)}

def convert_temperature(value, from_unit, to_unit):
    multiplier, divisor, offset = conversion_factors[f'{from_unit}to{to_unit}']
    return (value * multiplier + offset) // divisor
if __name__ == '__main__':
    sample_celsius = 25
    sample_fahrenheit = 77
    print(convert_temperature(sample_celsius, 'C', 'F'))
    print(convert_temperature(sample_fahrenheit, 'F', 'C'))