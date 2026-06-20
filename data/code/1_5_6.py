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
        'person1': {
            'name': 'Alice',
            'weights': [50.5, 51.0, 49.8]
        },
        'person2': {
            'name': 'Bob',
            'record': {
                'initial': 80.0,
                'final': 75.5,
                'notes': 'not a number'
            }
        },
        'group': [
            {'weight': 60.2},
            {'weight': 65.7, 'extra': [10, 20]}
        ],
        'metadata': {
            'total_records': 3,
            'description': 'Test data'
        }
    }
    result = extract_weights(sample_data)
    print(result)