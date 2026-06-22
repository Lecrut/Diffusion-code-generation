def validate_weights(weights):
    if not all(isinstance(weight, (int, float)) for weight in weights):
        raise ValueError("All elements in the list must be integers or floats")

def grams_to_ounces(grams):
    validate_weights(grams)
    return [g / 28.3495 for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    print(grams_to_ounces(sample_weights))