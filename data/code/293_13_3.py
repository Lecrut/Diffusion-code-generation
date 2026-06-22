def convert_to_kg(weight, unit):
    conversion_factors = {'kg': 1, 'lb': 0.453592}
    if unit not in conversion_factors:
        raise ValueError('Invalid unit. Supported units are "kg" and "lb".')
    return weight * conversion_factors[unit]

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
    print(compare_weights(1, 'kg', 2, 'kg'))