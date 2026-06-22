def validate_weights(weight_list):
    if not all(isinstance(w, (int, float)) for w in weight_list):
        raise ValueError("All elements in the list must be integers or floats.")

def grams_to_ounces(grams):
    validate_weights(grams)
    return [g / 28.3495 for g in grams]

if __name__ == '__main__':
    sample_weights = [100, 200, 300]
    print(grams_to_ounces(sample_weights))