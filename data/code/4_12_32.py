def convert_distance(value, unit):
    if unit == 'meters_to_kilometers':
        return value / 1000
    elif unit == 'kilometers_to_meters':
        return value * 1000
    else:
        raise ValueError("Unsupported conversion unit")

if __name__ == '__main__':
    sample_values = [
        (1500, 'meters_to_kilometers'),
        (2.5, 'kilometers_to_meters')
    ]
    
    for value, unit in sample_values:
        converted_value = convert_distance(value, unit)
        print(f"{value} {unit.split('_to_')[0]} is {converted_value} {unit.split('_to_')[1]}")