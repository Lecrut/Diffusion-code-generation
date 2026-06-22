def convert_kg_to_pounds(weights_kg):
    conversion_factor = 2.20462
    return [weight * conversion_factor for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [1.0, 2.5, 5.0, 10.0, 25.5, 100.0]
    converted_weights = convert_kg_to_pounds(sample_weights)
    print(converted_weights)