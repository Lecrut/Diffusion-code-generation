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
            'weights': [70, 72, 68],
            'details': {
                'age': 30,
                'height': 175
            }
        },
        'person2': {
            'weights': [65.5, 66, 64.5],
            'details': {
                'age': 28,
                'height': 165
            }
        },
        'person3': {
            'weights': [80, 79, 81],
            'details': {
                'age': 35,
                'height': 180
            }
        }
    }
    
    weights = extract_weights(sample_data)
    print(weights)