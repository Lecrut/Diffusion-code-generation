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
        "user_details": {
            "name": "Alice",
            "age": 30,
            "city": "New York"
        },
        "product_info": {
            "id": 101,
            "price": 29.99,
            "in_stock": True
        },
        "settings": "dark_mode"
    }
    simple_values = map_to_simple_values(sample_data)
    print(simple_values)