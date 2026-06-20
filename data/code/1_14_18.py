def kilograms_to_pounds(weights_kg):
    conversion_factor = 2.20462
    return [weight * conversion_factor for weight in weights_kg]
if __name__ == '__main__':
    sample_weights_kg = [0, 1, 5, 10, 15.5, 100, -5]
    converted_weights = kilograms_to_pounds(sample_weights_kg)
    print(converted_weights)