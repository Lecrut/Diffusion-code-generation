def convert_kilograms_to_pounds(weights_kg):
    conversion_factor = 2.20462
    return [weight * conversion_factor for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [0.5, 1.5, 2.5, 3.5]
    converted_weights = convert_kilograms_to_pounds(sample_weights)
    print(converted_weights)