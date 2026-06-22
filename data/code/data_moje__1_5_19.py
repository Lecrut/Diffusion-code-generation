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
            'q1': {'jan': [70, 71, 69], 'feb': 72, 'mar': [73, 74]},
            'q2': {'apr': 75, 'may': [76, 75.5], 'jun': 77}
        },
        'year_2021': {
            'q1': {'jan': [78, 79], 'feb': 80, 'mar': 81},
            'q2': {'apr': [82, 83], 'may': 84, 'jun': 85}
        },
        'metadata': {'unit': 'kg', 'source': 'scale'}
    }
    result = extract_weights(sample_data)
    print(result)