def extract_weights(data):
    result = []
    if isinstance(data, dict):
        for value in data.values():
            result.extend(extract_weights(value))
    elif isinstance(data, list):
        for item in data:
            result.extend(extract_weights(item))
    elif isinstance(data, (int, float)):
        result.append(data)
    return result

if __name__ == '__main__':
    sample_data = {
        "user1": {"weight": 70.5, "history": [68, 69, 70.5]},
        "user2": {"stats": {"current": 80, "previous": [75, 76.2]}, "active": True},
        "nested": {"level1": {"level2": {"weight": 90}}},
        "empty_list": [],
        "mixed": [10, {"val": 20}, [30]]
    }
    extracted = extract_weights(sample_data)
    print(extracted)