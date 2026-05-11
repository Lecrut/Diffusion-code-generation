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
        "user_profile": {
            "name": "Alice",
            "age": 30,
            "city": "New York"
        },
        "settings": {
            "theme": "dark",
            "notifications": True
        },
        "status": "active"
    }
    simple_values = map_to_simple_values(sample_data)
    print(simple_values)