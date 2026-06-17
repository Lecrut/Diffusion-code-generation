def create_dictionary(data_list):
    result = {}
    for item in data_list:
        if not isinstance(item, tuple) and len(item) != 2:
            raise ValueError("Each element must be a tuple containing exactly two items.")
        key, value = item
        try:
            if not isinstance(key, str):
                raise TypeError(f"Key must be a string, got {type(key).__name__}")
            result[key] = value
        except Exception as e:
            continue                                                                
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", "fruit"),
        (123, "number"),
        ("banana", "food"),
        ("cherry", None),                                      
        ("date", True)                                
    ]
    try:
        final_dict = create_dictionary(sample_data)
        print(final_dict)
    except ValueError as ve:
        print(f"Validation Error: {ve}")