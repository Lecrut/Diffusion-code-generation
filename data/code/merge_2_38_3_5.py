import json
def construct_dict(iterable):
    result = {}
    for item in iterable:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item
            try:
                k_type, v_type = type(key), type(value)
                if not (isinstance(k_type, type) and issubclass(k_type, str)):
                    raise TypeError("Key must be a string")
                result[key] = value
            except Exception as e:
                print(f"Error processing {item}: {e}")
        else:
            continue
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        ("banana", None),
        ("cherry", "fruit"),
        (None, "error_key")
    ]
    constructed_dict = construct_dict(sample_data)
    print(json.dumps(constructed_dict))