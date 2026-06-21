def validate_data(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if not (isinstance(key, str) and isinstance(value, bool)):
                return False
        return True
    elif isinstance(data, list):
        for item in data:
            if not isinstance(item, bool):
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    sample_data = {
        "key1": True,
        "key2": False,
        "key3": {
            "subkey1": True,
            "subkey2": False
        },
        "key4": [True, False]
    }
    print(validate_data(sample_data))