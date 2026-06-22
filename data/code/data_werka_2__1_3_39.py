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
        'individual': {
            'basic_info': {
                'age': 30,
                'weight': 75
            },
            'medical_records': [
                {'visit_date': '2022-12-01', 'weight': 74},
                {'visit_date': '2022-12-02', 'notes': {'initial_weight': 73}}
            ]
        }
    }
    print(extract_weights(sample_data))