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
        "config_B": {"setting1": 20, "setting2": "off"},
        "simple_C": 30,
        "simple_D": "text"
    }
    simple_values = map_to_simple_values(sample_data)
    print(simple_values)