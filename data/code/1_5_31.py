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
            'records': [
                {'date': '2021-01-01', 'weight': 61.0},
                {'date': '2021-02-01', 'weight': 61.5}
            ]
        },
        'person2': {
            'weights': [70.0, 72.5],
            'records': [
                {'date': '2021-01-01', 'weight': 70.5},
                {'date': '2021-02-01', 'weight': 71.0}
            ]
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)