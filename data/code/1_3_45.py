def extract_weights(data):
    def is_valid_weight(value):
        return isinstance(value, (int, float))

    def recursive_extract(d):
        if isinstance(d, dict):
            for key, value in d.items():
                yield from recursive_extract(value)
        elif isinstance(d, list):
            for item in d:
                yield from recursive_extract(item)
        elif is_valid_weight(d):
            yield d

    return list(recursive_extract(data))

if __name__ == '__main__':
    sample_data = {
        'user1': {
            'profile': {
                'age': 30,
                'weight': 75
            },
            'medical_records': [
                {'date': '2022-01-01', 'weight': 74},
                {'date': '2022-02-01', 'notes': {'initial_weight': 73}}
            ]
        },
        'user2': {
            'details': {
                'gender': 'female',
                'weight': 65
            }
        }
    }

    weights = extract_weights(sample_data)
    print(weights)