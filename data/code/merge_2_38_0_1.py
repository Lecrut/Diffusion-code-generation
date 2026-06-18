def create_dictionary(data_list):
    result = {}
    for item in data_list:
        if not isinstance(item, tuple) and len(item) != 2:
            raise ValueError("Each element must be a tuple containing exactly two items.")
        key, value = item
        if not isinstance(key, str):
            raise TypeError(f"Key must be a string, got {type(key).__name__}.")
        result[key] = value
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        ("banana", 20),
        ("cherry", "fresh"),
        (456, None)                                                   
    ]
    try:
        my_dict = create_dictionary(sample_data[:3])
        print(my_dict)
    except Exception as e:
        print(f"Error occurred: {e}")