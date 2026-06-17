def create_dictionary(data_list):
    result = {}
    for item in data_list:
        if not isinstance(item, tuple) and len(item) != 2:
            raise ValueError("Each element must be a tuple of exactly two elements.")
        key, value = item
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}.")
        try:
            float(value)
        except (TypeError, ValueError):
            pass
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        ("banana", "20"),
        ("cherry", None),
        ("date", True),
        ("elderberry", -5.5)
    ]
    try:
        dictionary_result = create_dictionary(sample_data)
        print(dictionary_result)
    except Exception as e:
        print(f"Error occurred while creating the dictionary: {e}")