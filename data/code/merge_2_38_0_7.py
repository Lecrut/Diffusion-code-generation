def create_dictionary(tuples_list):
    result = {}
    for item in tuples_list:
        if not isinstance(item, tuple) and len(item) != 2:
            raise ValueError("Each element must be a tuple containing exactly two elements.")
        key, value = item
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}.")
        result[key] = value
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        (5, "five"),
        ("banana", 20.5),
        ("cherry", True)
    ]
    try:
        final_dict = create_dictionary(sample_data + [("invalid_key", None)]) 
        print(final_dict)
    except (ValueError, TypeError):
        pass
    valid_sample = [
        ("fruit_a", "red"),
        ("number_123", 456),
        ("active_user", True)
    ]
    dictionary_result = create_dictionary(valid_sample)
    print(dictionary_result)