OZ_PER_KG = 35.274

def convert_weights_to_ounces(weights):
    if isinstance(weights, dict):
        return {item: convert_weights_to_ounces(weight) for item, weight in weights.items()}
    else:
        return weights * OZ_PER_KG

if __name__ == '__main__':
    sample_weights = {
        'apple': 0.5,
        'banana': 1.2,
        'nested': {
            'grape': 0.05,
            'orange': 0.3
        }
    }
    converted_weights = convert_weights_to_ounces(sample_weights)
    print(converted_weights)