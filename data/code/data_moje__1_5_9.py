def extract_weights(data):
    if isinstance(data, dict):
        result = []
        for key, value in data.items():
            result.extend(extract_weights(value))
        return result
    elif isinstance(data, list):
        result = []
        for item in data:
            result.extend(extract_weights(item))
        return result
    elif isinstance(data, (int, float)):
        return [data]
    else:
        return []

if __name__ == '__main__':
    sample_data = {
        'subject_a': {
            'weights': [150.5, 152.3, {'day': 1, 'value': 149.0}],
            'metadata': 'info'
        },
        'subject_b': {
            'weights': 180.0,
            'notes': None
        }
    }
    print(extract_weights(sample_data))