def extract_weights(data):
    results = []
    if isinstance(data, dict):
        for key, value in data.items():
            results.extend(extract_weights(value))
    elif isinstance(data, list):
        for item in data:
            results.extend(extract_weights(item))
    elif isinstance(data, (int, float)):
        results.append(data)
    return results

if __name__ == '__main__':
    sample_data = {
        "patient_1": {
            "measurements": [
                {"type": "weight", "value": 150.5, "unit": "lbs"},
                {"type": "weight", "value": 152.0, "unit": "lbs"}
            ]
        },
        "patient_2": {
            "measurements": [
                {"type": "weight", "value": 180.25, "unit": "lbs"}
            ]
        },
        "metadata": {
            "count": 2,
            "status": "active"
        }
    }
    print(extract_weights(sample_data))