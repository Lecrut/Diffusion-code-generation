def convert_kg_to_lb(weights_kg):
    conversion_factor = 2.20462
    return [weight * conversion_factor for weight in weights_kg]
if __name__ == '__main__':
    sample_weights_kg = [1, 5, 10, 20]
    converted_weights_lb = convert_kg_to_lb(sample_weights_kg)
    print(converted_weights_lb)