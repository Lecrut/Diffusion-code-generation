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
            'name': 'Alice',
            'measurements': [70.5, 68.2, {'baseline': 72.0}]
        },
        'person2': {
            'name': 'Bob',
            'weight': 85.3,
            'history': {
                '2020': 82.1,
                '2021': 84.5
            }
        },
        'team_avg': 78.9
    }
    result = extract_weights(sample_data)
    print(result)