CONVERSION_FACTORS = {'kg': 1, 'lb': 0.453592}

def convert_to_kg(weight, unit):
    if unit not in CONVERSION_FACTORS:
        raise ValueError('Invalid unit. Supported units are "kg" and "lb".')
    return weight * CONVERSION_FACTORS[unit]

def compare_weights(weight1, unit1, weight2, unit2):
    try:
        weight1_kg = convert_to_kg(weight1, unit1)
        weight2_kg = convert_to_kg(weight2, unit2)
    except ValueError as e:
        return str(e)
    
    if weight1_kg > weight2_kg:
        return f'{weight1} {unit1}'
    elif weight1_kg < weight2_kg:
        return f'{weight2} {unit2}'
    else:
        return 'Equal'

if __name__ == '__main__':
    print(compare_weights(10, 'kg', 22, 'lb'))
    print(compare_weights(5, 'lb', 2.3, 'kg'))