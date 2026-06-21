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
            'weights': [60, 62, 65],
            'details': {
                'height': 175,
                'weight': 68
            }
        },
        'person2': {
            'weights': [55, 57, 60],
            'details': {
                'height': 165,
                'notes': {
                    'last_weight': 59
                }
            }
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)