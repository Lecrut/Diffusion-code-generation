def extract_weight_values(data):
    weights = []
    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weight_values(value))
    elif isinstance(data, list):
        for item in data:
            weights.extend(extract_weight_values(item))
    elif isinstance(data, (int, float)) and not isinstance(data, bool):
        weights.append(data)
    return weights

if __name__ == '__main__':
    sample_data = {
        "patient_a": {"weight": 70.5, "history": [65.2, 68.0]},
        "patient_b": {
            "details": {
                "weight": 82.0,
                "records": [{"w": 81.5}, {"w": 83.2}]
            },
            "other_weight": 80.0
        },
        "empty_record": {},
        "nested_empty": {"data": []}
    }
    result = extract_weight_values(sample_data)
    print(result)