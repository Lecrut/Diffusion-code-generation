def extract_weights(nested_dict):
    weights = []
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            weights.extend(extract_weights(value))
        elif isinstance(value, (int, float)):
            weights.append(value)
    return weights

if __name__ == '__main__':
    sample_data = {
        'person1': {
            'weight': 70,
            'children': {
                'child1': {'weight': 30},
                'child2': {'weight': 35, 'additional_info': {'height': 150}}
            }
        },
        'person2': {
            'weight': 65,
            'pets': {
                'dog': {'weight': 10}
            }
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)