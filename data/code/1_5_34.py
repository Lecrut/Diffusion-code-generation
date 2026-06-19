def extract_weights(nested_dict):
    weights = []
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            weights.extend(extract_weights(value))
        elif isinstance(value, (int, float)):
            weights.append(value)
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
            }
        },
        'person2': {
            'weight': 65.5,
            'details': {
                'height': 165,
                'measurements': {
                    'waist': 75,
                    'hips': 85
                }
            }
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)