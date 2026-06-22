def convert_distance(value, unit):
    conversion_factors = {
        ('m', 'km'): 1 / 1000,
        ('km', 'm'): 1000
    }
    
    if (unit[0], unit[1]) in conversion_factors:
        return value * conversion_factors[(unit[0], unit[1])]
    else:
        raise ValueError("Unsupported units. Use a tuple like ('m', 'km') for meters to kilometers or ('km', 'm') for kilometers to meters.")

if __name__ == '__main__':
    sample_values = [
        (1500, ('m', 'km')),
        (2.5, ('km', 'm'))
    ]
    for value, unit in sample_values:
        converted_value = convert_distance(value, unit)
        print(f"{value} {unit[0]} is equal to {converted_value} {unit[1]}")