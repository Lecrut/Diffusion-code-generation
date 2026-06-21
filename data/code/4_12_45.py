def convert_distance(value, unit):
    conversion_factors = {'m': 1 / 1000, 'km': 1000}
    if unit not in conversion_factors:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")
    return value * conversion_factors[unit]
if __name__ == '__main__':
    sample_values = [(1500, 'm'), (2.5, 'km')]
    for value, unit in sample_values:
        converted_value = convert_distance(value, unit)
        if unit == 'm':
            print(f'{value} meters is {converted_value} kilometers')
        else:
            print(f'{value} kilometers is {converted_value} meters')