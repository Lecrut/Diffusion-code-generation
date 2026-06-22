CONVERSION_FACTOR = 2.20462

def convert_kg_to_lb(weights_kg):
    if not all(isinstance(weight, (int, float)) for weight in weights_kg):
        raise ValueError("All weights must be numbers")
    return [weight * CONVERSION_FACTOR for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [2.5, 7.3, 15.0, 30.5]
    converted_weights = convert_kg_to_lb(sample_weights)
    print(converted_weights)