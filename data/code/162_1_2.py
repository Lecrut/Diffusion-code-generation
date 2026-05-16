def map_to_simple_values(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = value
        else:
            result[key] = value
    return result
if __name__ == '__main__':
    sample_data = {
        "config_A": {"setting1": 10, "setting2": "on"},
        "config_B": 20,
        "config_C": {"value": 30}
    }
    simple_values = map_to_simple_values(sample_data)
    print(simple_values)