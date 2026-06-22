def extract_weights(data):
    weights = []
    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weights(value))
    elif isinstance(data, (list, tuple)):
        for item in data:
            weights.extend(extract_weights(item))
    elif isinstance(data, (int, float)) and not isinstance(data, bool):
        weights.append(data)
    return weights

if __name__ == '__main__':
    sample_data = {
        "user": {
            "name": "Alice",
            "stats": {
                "weight_kg": 65.5,
                "history": [62.0, 63.5, 64.0]
            }
        },
        "users": [
            {"id": 1, "weight": 70},
            {"id": 2, "details": {"weight": 55.2, "old_weight": 58}}
        ],
        "meta": {
            "count": 2,
            "threshold": 100
        }
    }
    result = extract_weights(sample_data)
    print(result)