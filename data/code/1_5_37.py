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
        'person1': {'weight': 70, 'details': {'height': 175}},
        'person2': [{'weight': 60}, {'details': {'weight': 80}}],
        'person3': {'info': {'nested': {'weight': 90}}}
    }
    print(extract_weights(sample_data))