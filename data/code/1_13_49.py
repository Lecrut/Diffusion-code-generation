CONVERSION_RATE = 2.20462

def convert_weights_kg_to_lb(weights_kg):
    return [weight * CONVERSION_RATE for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [2, 7, 15, 30]
    converted_weights_lb = convert_weights_kg_to_lb(sample_weights_kg)
    print(converted_weights_lb)