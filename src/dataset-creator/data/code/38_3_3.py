import json
def build_dict_from_iterable(data):
    result = {}
    for item in data:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item
            try:
                k_type, v_type = type(key), type(value)
                if not (isinstance(k_type, type) and issubclass(k_type, str)):
                    raise ValueError("Key must be a string")
                result[key] = value
            except Exception as e:
                print(f"Error processing {item}: {e}")
        else:
            continue
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        ("banana", None),
        (3, "invalid"),
        ("cherry", 20.5)
    ]
    output_dict = build_dict_from_iterable(sample_data)
    print(json.dumps(output_dict))