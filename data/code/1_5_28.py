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
        'user1': {'weight': 70, 'logs': [{'date': '2023-01-01', 'weight': 68}, {'date': '2023-01-02', 'notes': 'felt good'}]},
        'user2': {'logs': [{'date': '2023-01-01', 'weight': 65, 'notes': 'light workout'}, {'date': '2023-01-03', 'weight': 64}]},
        'user3': [72, {'date': '2023-01-01', 'weight': 71}, [{'date': '2023-01-02', 'weight': 70}]]
    }
    
    extracted_weights = extract_weights(sample_data)
    print(extracted_weights)