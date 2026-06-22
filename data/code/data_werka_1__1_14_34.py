def convert_kg_to_lb(weights_in_kg):
    conversion_factor = 2.20462
    return [weight * conversion_factor for weight in weights_in_kg]

if __name__ == '__main__':
    sample_weights_kg = [50, 75, 100, 120]
    converted_weights_lb = convert_kg_to_lb(sample_weights_kg)
    print(converted_weights_lb)