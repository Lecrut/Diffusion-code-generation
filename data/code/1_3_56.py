def extract_weights(nested_dict):
    weights = []
    if isinstance(nested_dict, dict):
        for key, value in nested_dict.items():
            weights.extend(extract_weights(value))
    elif isinstance(nested_dict, list):
        for item in nested_dict:
            weights.extend(extract_weights(item))
    elif isinstance(nested_dict, (int, float)):
        weights.append(nested_dict)
    return weights

if __name__ == '__main__':
    sample_data = {
        'person1': {
            'weights': [60.5, 62.3],
            'details': {
                'age': 30,
                'height': 175
            }
        },
        'person2': {
            'weights': [70.2, 68.9, {'year': 2022, 'weight': 71.0}],
            'details': {
                'age': 25,
                'height': 165
            }
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)