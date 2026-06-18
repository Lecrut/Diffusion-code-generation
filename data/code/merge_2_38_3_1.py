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
            try:
                key_str = json.dumps(item) if isinstance(item, (dict, list)) else str(item)
                val_type = type(item).__name__
                result[key_str] = None
            except Exception as e:
                print(f"Error processing {item}: {e}")
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", "fruit"),
        (123, 456),
        ["orange"],
        {"banana": None},
        ("grape", "berry")
    ]
    output_dict = build_dict_from_iterable(sample_data)
    print(json.dumps(output_dict))