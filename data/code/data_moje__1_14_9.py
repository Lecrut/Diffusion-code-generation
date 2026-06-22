def convert_kg_to_lbs(weights_kg):
    return [weight * 2.20462 for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [1, 10, 100, 0.5]
    result = convert_kg_to_lbs(sample_weights_kg)
    print(result)