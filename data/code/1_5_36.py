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
        'record1': {
            'weight': 70.5,
            'details': {
                'height': 175,
                'notes': 'Good health'
            }
        },
        'record2': {
            'weight': 68,
            'details': {
                'height': 165,
                'additional_records': {
                    'weight': 67.5
                }
            }
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)