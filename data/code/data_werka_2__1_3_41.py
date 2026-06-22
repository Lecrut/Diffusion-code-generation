def extract_weights(nested_dict):
    weights = []
    if isinstance(nested_dict, dict):
        for key, value in nested_dict.items():
            if isinstance(value, (int, float)):
                weights.append(value)
            elif isinstance(value, dict):
                weights.extend(extract_weights(value))
            elif isinstance(value, list):
                for item in value:
                    weights.extend(extract_weights(item))
    return weights

if __name__ == '__main__':
    sample_data = {
        'person1': {
            'weight': 70,
            'details': {
                'height': 175,
                'measurements': {
                    'waist': 80,
                    'hips': 90
                }
            },
            'history': [
                {'date': '2023-01-01', 'weight': 68},
                {'date': '2023-02-01', 'notes': 'gained weight'}
            ]
        },
        'person2': {
            'weight': 65,
            'details': {
                'height': 165,
                'measurements': {
                    'waist': 75,
                    'hips': 85
                }
            },
            'history': [
                {'date': '2023-01-01', 'weight': 64},
                {'date': '2023-02-01', 'notes': 'lost weight'}
            ]
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)