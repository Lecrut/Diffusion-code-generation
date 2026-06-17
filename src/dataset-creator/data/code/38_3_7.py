def build_dict_from_iterable(data):
    result = {}
    for item in data:
        if isinstance(item, tuple) and len(item) == 2:
            key, value = item
            try:
                k_type, v_type = type(key), type(value)
                if not (isinstance(k_type, type) and issubclass(k_type, object)):
                    raise ValueError("Invalid key")
                result[key] = value
            except Exception as e:
                print(f"Error processing {item}: {e}")
        else:
            continue
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        (None, "missing"),
        ((3.5,), "tuple_key_error"),
        ("banana", None)
    ]
    output_dict = build_dict_from_iterable(sample_data)
    print(output_dict)