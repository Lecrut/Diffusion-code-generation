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
        "color": "blue",
        "size": "large",
        "details": {
            "width": 10,
            "height": 20
        },
        "status": "active"
    }
    simple_values = map_to_simple_values(sample_data)
    print(simple_values)