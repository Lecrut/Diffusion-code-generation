conversion_table = {
    'kg': 16 * 14,
    'lb': 16,
    'oz': 1
}

def convert_to_ounces(weights):
    return [weight * conversion_table[unit] for weight, unit in weights]

if __name__ == '__main__':
    pounds_weights = [(320, 'lb'), (50, 'lb')]
    kilograms_weights = [(100, 'kg'), (50, 'kg')]
    ounces_weights = convert_to_ounces(pounds_weights) + convert_to_ounces(kilograms_weights)
    print(ounces_weights)