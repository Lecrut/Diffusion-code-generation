CONVERSION_RATE = {"kg_to_lb": 2.20462}

def convert_kg_to_lb(weights_kg):
    return [weight * CONVERSION_RATE["kg_to_lb"] for weight in weights_kg]

if __name__ == '__main__':
    sample_weights_kg = [30, 55, 85, 105]
    converted_weights_lb = convert_kg_to_lb(sample_weights_kg)
    print(converted_weights_lb)