def convert_distance(value, unit):
    if unit == 'm_to_km':
        return value / 1000
    elif unit == 'km_to_m':
        return value * 1000
    else:
        raise ValueError("Unsupported conversion unit")

if __name__ == '__main__':
    sample_values = [
        (1500, 'm_to_km'),
        (2.5, 'km_to_m')
    ]
    
    for value, unit in sample_values:
        converted_value = convert_distance(value, unit)
        print(f"{value} {unit.split('_to_')[0]} is {converted_value} {unit.split('_to_')[1]}")