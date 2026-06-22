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
            'weights': [70.5, 68.2],
            'notes': 'initial check'
        },
        'person2': {
            'weights': [
                {'date': '2023-01-01', 'weight': 80.0},
                {'date': '2023-02-01', 'weight': 79.5}
            ],
            'additional_info': {
                'family': {
                    'parent1': 65,
                    'parent2': 62
                }
            }
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)