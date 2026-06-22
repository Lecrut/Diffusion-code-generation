def extract_weights(data):
    def recursive_extract(d):
        if isinstance(d, dict):
            for key, value in d.items():
                yield from recursive_extract(value)
        elif isinstance(d, list):
            for item in d:
                yield from recursive_extract(item)
        elif isinstance(d, (int, float)):
            yield d

    return list(recursive_extract(data))

if __name__ == '__main__':
    sample_data = {
        'user': {
            'personal_info': {
                'height': 175,
                'weight': 80
            },
            'medical_records': [
                {'date': '2023-06-01', 'weight': 78},
                {'date': '2023-06-15', 'notes': {'initial_weight': 79}}
            ]
        }
    }
    weights = extract_weights(sample_data)
    print(weights)