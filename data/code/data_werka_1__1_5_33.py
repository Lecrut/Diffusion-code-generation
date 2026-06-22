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
            'weight': 70,
            'records': [
                {'date': '2023-01-01', 'weight': 68},
                {'date': '2023-01-02', 'notes': 'sick', 'weight': 72}
            ]
        },
        'person2': {
            'records': [
                {'date': '2023-01-01', 'weight': 65},
                {'date': '2023-01-02', 'weight': 64}
            ],
            'notes': 'underweight'
        }
    }
    print(extract_weights(sample_data))