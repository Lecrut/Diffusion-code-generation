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
        'person1': {'weight': 70.5, 'records': [{'date': '2023-01-01', 'weight': 68}, {'date': '2023-01-02'}]},
        'person2': {'details': {'weight': 80, 'history': [78.5, {'date': '2023-01-03', 'weight': 79}]}},
        'person3': [{'weight': 65}, {'notes': 'no weight data'}]
    }
    
    weights = extract_weights(sample_data)
    print(weights)