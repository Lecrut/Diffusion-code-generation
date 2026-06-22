def convert_to_kilograms(weight_measurements):
    conversion_factors = {'kg': 1, 'g': 0.001, 'lb': 0.453592, 'oz': 0.0283495, 'ton': 1000}
    converted_weights = []
    for weight, unit in weight_measurements:
        try:
            factor = conversion_factors[unit.lower()]
            converted_weight = weight * factor
            converted_weights.append(converted_weight)
        except KeyError:
            print(f"Warning: Unsupported unit '{unit}'. Skipping this measurement.")
    return converted_weights
if __name__ == '__main__':
    sample_weights = [(10, 'kg'), (500, 'g'), (200, 'lb'), (16, 'oz'), (1, 'ton'), (100, 'unknown')]
    converted_weights = convert_to_kilograms(sample_weights)
    print(converted_weights)