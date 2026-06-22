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
        'year_2020': {
            'q1': [70.5, 71.2],
            'q2': {'jan': 72.0, 'feb': [73.1, 72.8]}
        },
        'year_2021': {
            'monthly': {
                'm1': 74.5,
                'm2': {'weight': 75.0, 'note': 'healthy'}
            }
        },
        'extras': ['ignore', 100, {'nested': 50}]
    }
    result = extract_weights(sample_data)
    print(result)