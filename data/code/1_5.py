def extract_weights(data):
    weights = []
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (int, float)):
                weights.append(value)
            elif isinstance(value, dict):
                weights.extend(extract_weights(value))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (int, float)):
                weights.append(item)
            elif isinstance(item, dict):
                weights.extend(extract_weights(item))
    return weights
if __name__ == '__main__':
    weight_data = {
        "record_1": {
            "weight_kg": 75.5,
            "details": {
                "weight_lbs": 166.4,
                "notes": "heavy"
            },
            "status": "complete"
        },
        "record_2": {
            "weight_kg": 80.0,
            "details": {
                "weight_lbs": 176.4,
                "notes": "heavy"
            },
            "status": "pending"
        },
        "summary": [
            {"id": 1, "weight": 100.0},
            {"id": 2, "weight": 105.5}
        ]
    }
    result = extract_weights(weight_data)
    print(result)