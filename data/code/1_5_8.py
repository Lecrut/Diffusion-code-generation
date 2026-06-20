def extract_weights(nested_dict):
    weights = []
    if isinstance(nested_dict, dict):
        for value in nested_dict.values():
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
            'name': 'Alice',
            'weights': [70.5, 72.0, 71.5]
        },
        'person2': {
            'name': 'Bob',
            'record': {
                'year2020': 80.0,
                'year2021': 78.5
            }
        },
        'group': {
            'members': [
                {'weight': 65.0},
                {'weight': 90.2}
            ]
        },
        'metadata': 'not a number'
    }
    result = extract_weights(sample_data)
    print(result)