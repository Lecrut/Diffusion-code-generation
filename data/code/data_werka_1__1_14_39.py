def kilograms_to_pounds(weights_kg):
    conversion_factor = 2.20462
    return [weight * conversion_factor for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [50, 75, 100, 150]
    converted_weights_lb = kilograms_to_pounds(sample_weights_kg)
    print(converted_weights_lb)