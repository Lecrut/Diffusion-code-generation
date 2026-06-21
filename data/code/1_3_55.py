def extract_weights(data):
    weights = []
    
    def recursive_extract(d):
        if isinstance(d, dict):
            for key, value in d.items():
                recursive_extract(value)
        elif isinstance(d, list):
            for item in d:
                recursive_extract(item)
        elif isinstance(d, (int, float)):
            weights.append(d)
    
    recursive_extract(data)
    return weights

if __name__ == '__main__':
    sample_data = {
        'user': {
            'details': {
                'age': 30,
                'weight': 75
            },
            'medical_records': [
                {'date': '2023-01-01', 'weight': 74},
                {'date': '2023-01-02', 'notes': {'initial_weight': 76}}
            ],
            'family_members': [
                {'name': 'parent', 'details': {'age': 50, 'weight': 68}},
                {'name': 'sibling', 'details': {'age': 25, 'weight': 55}}
            ]
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)