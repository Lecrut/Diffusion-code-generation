def extract_weights(data):
    weights = []
    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weights(value))
    elif isinstance(data, (list, tuple)):
        for item in data:
            weights.extend(extract_weights(item))
    elif isinstance(data, (int, float)) and not isinstance(data, bool):
        weights.append(data)
    return weights

if __name__ == '__main__':
    sample_data = {
        'patient': 'John',
        'records': [
            {'week': 1, 'weight': 70.5},
            {'week': 2, 'weight': 71.2},
            {'nested': {'deep': {'value': 69.0}}}
        ],
        'units': 'kg'
    }
    result = extract_weights(sample_data)
    print(result)