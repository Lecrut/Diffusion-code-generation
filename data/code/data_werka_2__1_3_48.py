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
        else:
            raise ValueError(f"Unsupported data type: {type(d)}")
    return list(recursive_extract(data))

if __name__ == '__main__':
    sample_data = {
        'person1': {
            'weight': 70,
            'records': [
                {'date': '2023-01-01', 'weight': 68},
                {'date': '2023-01-02', 'notes': {'initial_weight': 69}}
            ]
        },
        'person2': {
            'details': [
                {'height': 180, 'weight': 75},
                {'history': [{'date': '2023-02-01', 'weight': 74}, {'date': '2023-02-02', 'notes': {'initial_weight': 76}}]}
            ]
        }
    }
    try:
        weights = extract_weights(sample_data)
        print(weights)
    except ValueError as e:
        print(e)