def create_dictionary(data_list):
    result = {}
    for item in data_list:
        if not isinstance(item, tuple) and len(item) != 2:
            raise ValueError("Each element must be a tuple containing exactly two items.")
        key, value = item[0], item[1]
        if not isinstance(key, (str, int)):
            raise TypeError(f"Key type {type(key).__name__} is invalid. Expected str or int.")
        result[key] = value
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        (5, "fruit"),
        ("banana", 20),
        ("cherry", 30)
    ]
    try:
        my_dict = create_dictionary(sample_data)
        print(my_dict)
    except Exception as e:
        print(f"Error occurred: {e}")