def validate_weights(weights):
    if not all(isinstance(weight, (int, float)) for weight in weights):
        raise ValueError("All weights must be numbers.")

def grams_to_ounces(grams):
    return grams * 0.035274

def convert_weights(weights):
    validate_weights(weights)
    return [round(grams_to_ounces(weight), 2) for weight in weights]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    converted_weights = convert_weights(sample_weights)
    print(f"Converted weights: {converted_weights}")