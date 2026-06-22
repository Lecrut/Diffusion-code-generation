def convert_weights_to_ounces(weights):
    ounces_per_kg = 35.274
    if isinstance(weights, dict):
        return {item: weight * ounces_per_kg for item, weight in weights.items()}
    else:
        raise ValueError("Input must be a dictionary with item names as keys and weights in kilograms as values.")

if __name__ == '__main__':
    sample_weights = {
        "apple": 0.5,
        "banana": 1.2,
        "carrot": 0.3,
        "date": 0.05
    }
    converted_weights = convert_weights_to_ounces(sample_weights)
    print(converted_weights)