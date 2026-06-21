CONVERSION_RATE = {"kg_to_lb": 2.20462}

def convert_weights(weights_kg):
    return [weight * CONVERSION_RATE["kg_to_lb"] for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [30, 55, 80, 105]
    converted_weights_lb = convert_weights(sample_weights_kg)
    print(converted_weights_lb)