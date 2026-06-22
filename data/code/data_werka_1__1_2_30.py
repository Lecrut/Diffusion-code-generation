def convert_to_kilograms(weight_measurements):
    conversion_factors = {'kg': 1, 'g': 0.001, 'lb': 0.453592, 'oz': 0.0283495, 'ton': 1000}
    converted_weights = []
    for weight, unit in weight_measurements:
        try:
            if unit not in conversion_factors:
                raise ValueError(f'Unknown unit: {unit}')
            converted_weight = weight * conversion_factors[unit]
            converted_weights.append(converted_weight)
        except Exception as e:
            print(f'Error converting {weight} {unit}: {e}')
    return converted_weights
if __name__ == '__main__':
    sample_weights = [(10, 'kg'), (2500, 'g'), (150, 'lb'), (8, 'oz'), (0.5, 'ton'), (100, 'unknown')]
    converted_weights = convert_to_kilograms(sample_weights)
    print(converted_weights)