def validate_data(data):
    if isinstance(data, dict):
        return all(validate_data(v) for v in data.values())
    elif isinstance(data, list):
        return all(validate_data(v) for v in data)
    elif isinstance(data, str):
        return len(data) > 0 and data.isalpha()
    elif isinstance(data, int):
        return data >= 0
    else:
        return False

if __name__ == '__main__':
    sample_data = {
        "name": "John",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown"
        },
        "contacts": [
            {"type": "email", "value": "john@example.com"},
            {"type": "phone", "value": "123-456-7890"}
        ]
    }
    print(validate_data(sample_data))