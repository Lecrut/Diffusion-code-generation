def compare_weights(weight1, unit1, weight2, unit2):
    conversion_factors = {'kg': 1, 'lb': 0.453592}
    weight1_converted = weight1 * conversion_factors[unit1]
    weight2_converted = weight2 * conversion_factors[unit2]
    if weight1_converted > weight2_converted:
        return f'{weight1} {unit1}'
    elif weight1_converted < weight2_converted:
        return f'{weight2} {unit2}'
    else:
        return 'Equal'
if __name__ == '__main__':
    print(compare_weights(10, 'kg', 22, 'lb'))
    print(compare_weights(5, 'lb', 2.3, 'kg'))
    print(compare_weights(7, 'kg', 7, 'kg'))