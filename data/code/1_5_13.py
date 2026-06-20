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
            'weights': [70, 72.5, 71]
        },
        'person2': {
            'name': 'Bob',
            'weights': [80, 81]
        },
        'nested': {
            'group': {
                'weights': [65, 66.2]
            }
        }
    }
    print(extract_weights(sample_data))