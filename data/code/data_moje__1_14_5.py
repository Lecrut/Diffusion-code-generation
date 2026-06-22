CONVERSION_RATE = 2.20462

def convert_kg_to_lbs(weights_kg):
    return [weight * CONVERSION_RATE for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [10, 20, 30, 40, 50]
    converted_weights = convert_kg_to_lbs(sample_weights_kg)
    print(converted_weights)