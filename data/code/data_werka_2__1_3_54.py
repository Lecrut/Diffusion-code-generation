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
            'weights': [60.5, 62.3],
            'details': {
                'age': 30,
                'height': 175
            }
        },
        'person2': {
            'weights': [70.2, 68.9, 71.0],
            'details': {
                'age': 25,
                'height': 180
            }
        },
        'person3': {
            'weights': [
                {'year': 2020, 'weight': 55.0},
                {'year': 2021, 'weight': 57.5}
            ],
            'details': {
                'age': 40,
                'height': 165
            }
        }
    }

    weights = extract_weights(sample_data)
    print(weights)