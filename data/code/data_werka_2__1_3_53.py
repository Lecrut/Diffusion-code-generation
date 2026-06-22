def extract_weights(data):
    if isinstance(data, dict):
        weights = []
        for key, value in data.items():
            weights.extend(extract_weights(value))
        return weights
    elif isinstance(data, list):
        weights = []
        for item in data:
            weights.extend(extract_weights(item))
        return weights
    elif isinstance(data, (int, float)):
        return [data]
    else:
        raise ValueError("Unsupported data type")

if __name__ == '__main__':
    sample_data = {
        "person1": {"weight": 70, "details": {"height": 175}},
        "person2": [{"weight": 60}, {"details": {"weight": 80}}],
        "person3": {"info": {"nested": {"weight": 90}}}
    }
    
    weights = extract_weights(sample_data)
    print(weights)