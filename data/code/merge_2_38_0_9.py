def create_dictionary(tuples_list):
    result = {}
    for item in tuples_list:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Each element must be a tuple of exactly two elements.")
        key, value = item
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}.")
        try:
            result[key] = float(value)
        except (ValueError, OverflowError):
            raise ValueError(f"Invalid numeric value for key '{key}': {value}")
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", "1.5"),
        ("banana", "2.0"),
        ("cherry", "3.7")
    ]
    dictionary_result = create_dictionary(sample_data)
    print(dictionary_result)