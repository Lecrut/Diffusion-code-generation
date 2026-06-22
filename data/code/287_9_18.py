def convert_weights_to_ounces(weights):
    ounces_per_kg = 35.274
    if not isinstance(weights, dict):
        raise ValueError("Input must be a dictionary.")
    new_weights = {}
    for item, weight in weights.items():
        if isinstance(weight, dict):
            new_weights[item] = convert_weights_to_ounces(weight)
        elif isinstance(weight, (int, float)):
            new_weights[item] = weight * ounces_per_kg
        else:
            raise ValueError("Dictionary values must be numbers or nested dictionaries.")
    return new_weights

if __name__ == '__main__':
    sample_weights = {
        'apple': 1.2,
        'banana': 0.3,
        'box': {
            'notebook': 0.5,
            'pen': 0.2
        }
    }
    print(convert_weights_to_ounces(sample_weights))