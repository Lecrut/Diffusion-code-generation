def create_dictionary(data_list):
    result = {}
    if not isinstance(data_list, list) or len(data_list) == 0:
        return None
    for i in range(0, len(data_list), 2):
        key_val_pair = data_list[i]
        try:
            if not (isinstance(key_val_pair, tuple) and len(key_val_pair) == 2):
                raise ValueError(f"Invalid pair at index {i}: expected a tuple of two elements")
            k, v = key_val_pair[0], key_val_pair[1]
            if isinstance(k, str) or not (isinstance(k, int) and isinstance(v, (int, float))):
                result[k] = v
            else:
                raise ValueError(f"Invalid data type at index {i}: keys must be strings")
        except Exception as e:
            print(f"Validation error: {e}")
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", 1),
        ("banana", "fruit"),
        ("cherry", 2.5)
    ]
    try:
        final_dict = create_dictionary(sample_data)
        print(final_dict) if final_dict else print("No valid dictionary created")
    except Exception as e:
        pass