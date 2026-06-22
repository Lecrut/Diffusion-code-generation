def kilograms_to_pounds(weights_kg):
    return [weight * 2.20462 for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [50, 75, 100, 150]
    converted_weights = kilograms_to_pounds(sample_weights_kg)
    print(converted_weights)