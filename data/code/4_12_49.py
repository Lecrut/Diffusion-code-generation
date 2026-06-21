def convert_distance(value, unit):
    if unit == 'm':
        return value / 1000
    elif unit == 'km':
        return value * 1000
    else:
        raise ValueError("Unsupported unit. Use 'm' for meters or 'km' for kilometers.")
if __name__ == '__main__':
    sample_values = [(3000, 'm'), (5.0, 'km')]
    for value, unit in sample_values:
        converted_value = convert_distance(value, unit)
        target_unit = 'km' if unit == 'm' else 'm'
        print(f'{value} {unit} is equal to {converted_value} {target_unit}')