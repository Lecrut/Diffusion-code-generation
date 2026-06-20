def extract_weights(data):
    weights = []
    if isinstance(data, dict):
        for key in data:
            values = extract_weights(data[key])
            weights.extend(values)
    elif isinstance(data, list):
        for item in data:
            values = extract_weights(item)
            weights.extend(values)
    elif isinstance(data, (int, float)):
        weights.append(data)
    return weights

def main():
    sample_data = {
        "patient_1": {
            "history": [150.5, 148.0],
            "current": 145.2,
            "metadata": {
                "recorded_at": "2023-01-01",
                "unit": "lbs"
            }
        },
        "patient_2": {
            "history": [200.0, 195.5],
            "current": 190.1
        }
    }
    result = extract_weights(sample_data)
    print(result)

if __name__ == '__main__':
    main()