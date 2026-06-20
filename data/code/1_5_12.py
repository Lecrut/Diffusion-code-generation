def extract_weights(data):
    if isinstance(data, dict):
        weights = []
        for key, value in data.items():
            weights.extend(extract_weights(value))
        return weights
    elif isinstance(data, list):
        weights = []
        for item in data:
            weights.extend(extract_weights(item))
        return weights
    elif isinstance(data, (int, float)):
        return [data]
    else:
        return []

if __name__ == '__main__':
    sample_data = {
        'patient_1': {
            'record_1': {'weight': 70.5, 'unit': 'kg'},
            'record_2': 68.2
        },
        'patient_2': [
            {'weight': 80},
            {'weight': 82.5, 'notes': 'heavy'}
        ],
        'metadata': {'version': 1}
    }
    print(extract_weights(sample_data))