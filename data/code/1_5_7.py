def extract_weight_values(record):
    weights = []
    if isinstance(record, dict):
        for value in record.values():
            weights.extend(extract_weight_values(value))
    elif isinstance(record, list):
        for item in record:
            weights.extend(extract_weight_values(item))
    elif isinstance(record, (int, float)):
        weights.append(record)
    return weights

if __name__ == '__main__':
    sample_data = {
        "patient_1": {
            "name": "Alice",
            "weight_kg": 70.5,
            "records": [
                {"day": 1, "weight": 70.0},
                {"day": 2, "weight": 70.2}
            ]
        },
        "patient_2": {
            "name": "Bob",
            "details": {
                "current": 85.0,
                "history": [84.5, 84.8, None, 85.2]
            }
        },
        "meta": {
            "units": "kg",
            "count": 2
        }
    }
    result = extract_weight_values(sample_data)
    print(result)