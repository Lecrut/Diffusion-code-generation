def extract_weights(data):
    weights = []
    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weights(value))
    elif isinstance(data, list):
        for item in data:
            weights.extend(extract_weights(item))
    elif isinstance(data, (int, float)) and not isinstance(data, bool):
        weights.append(data)
    return weights

if __name__ == '__main__':
    sample = {
        'person1': {
            'name': 'Alice',
            'weights': [65.2, 64.8, {'current': 65.0}]
        },
        'person2': {
            'name': 'Bob',
            'weights': [[70.5, 71.0], {'history': [69.5, 70.0]}]
        },
        'metadata': {
            'total_entries': 2,
            'active': True
        }
    }
    print(extract_weights(sample))