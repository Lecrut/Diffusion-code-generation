def extract_weights(data):
    weights = []
    if isinstance(data, dict):
        for key, value in data.items():
            weights.extend(extract_weights(value))
    elif isinstance(data, list):
        for item in data:
            weights.extend(extract_weights(item))
    elif isinstance(data, (int, float)):
        weights.append(data)
    return weights

if __name__ == '__main__':
    sample_data = {
        'person1': {
            'weights': [60.5, 62.3],
            'children': [
                {'weight': 25.7},
                {'weight': 28.4}
            ]
        },
        'person2': {
            'weights': [70.2],
            'partner': {
                'weight': 65.0
            }
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)