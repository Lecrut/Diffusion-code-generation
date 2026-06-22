def extract_weights(data):
    weights = []
    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weights(value))
    elif isinstance(data, (int, float)):
        weights.append(data)
    elif isinstance(data, list):
        for item in data:
            weights.extend(extract_weights(item))
    return weights

if __name__ == '__main__':
    sample_data = {
        'person1': {
            'name': 'Alice',
            'weights': [70.5, 71.2, 70.8]
        },
        'person2': {
            'name': 'Bob',
            'weights': {
                'jan': 80,
                'feb': 79.5,
                'mar': {
                    'start': 79,
                    'end': 78
                }
            }
        },
        'group': {
            'total': 150,
            'members': [
                {'weight': 60},
                {'weight': 65.5}
            ]
        }
    }
    print(extract_weights(sample_data))