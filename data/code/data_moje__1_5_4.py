def extract_weights(data):
    weights = []
    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weights(value))
    elif isinstance(data, list):
        for item in data:
            weights.extend(extract_weights(item))
    elif isinstance(data, (int, float)):
        weights.append(data)
    return weights

if __name__ == '__main__':
    sample_data = {
        'subject1': {
            'weight': 75.5,
            'history': [74.0, 73.5],
            'details': {
                'ideal_weight': 70.0
            }
        },
        'subject2': {
            'weight': 60.0,
            'history': [61.0, 62.5, {'temp_weight': 63.0}]
        }
    }
    result = extract_weights(sample_data)
    print(result)