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
        "person1": {
            "current": 70.5,
            "history": [68.2, 69.1, 70.5]
        },
        "person2": {
            "current": 82.3,
            "previous": {
                "year1": 85.0,
                "year2": 84.2
            }
        },
        "group": [
            {"name": "Alice", "weight": 65.5},
            {"name": "Bob", "weight": 90.1}
        ]
    }
    result = extract_weights(sample_data)
    print(result)