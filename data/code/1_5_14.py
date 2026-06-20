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
            'measurements': {
                'weight_kg': 65.5,
                'height_cm': 170,
                'history': [
                    {'date': '2023-01-01', 'weight_kg': 64.0},
                    {'date': '2023-06-01', 'weight_kg': 65.5},
                    {'nested_extra': {'weight_kg': 63.0}}
                ]
            }
        },
        'person2': {
            'name': 'Bob',
            'weight_kg': 80.0
        },
        'group_average': 72.5
    }
    result = extract_weights(sample_data)
    print(result)