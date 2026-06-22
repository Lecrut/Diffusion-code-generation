KG_TO_OZ = 35.274

def convert_weights_to_ounces(weights):
    if not isinstance(weights, dict):
        raise ValueError('Input must be a dictionary')
    converted_weights = {}
    for item, weight in weights.items():
        if isinstance(weight, dict):
            converted_weights[item] = convert_weights_to_ounces(weight)
        else:
            try:
                converted_weights[item] = weight * KG_TO_OZ
            except TypeError:
                raise ValueError('Weights must be numbers')
    return converted_weights
if __name__ == '__main__':
    sample_weights = {'apple': 0.25, 'banana': {'small': 0.1, 'large': 0.15}, 'carrot': [0.05, 0.03], 'grape': {'red': 0.01, 'green': 0.01}}
    print(convert_weights_to_ounces(sample_weights))