def transform_flat_list(data):
    if len(data) % 2 != 0:
        raise ValueError("List length must be even to pair keys with values.")
    result = []
    for i in range(0, len(data), 2):
        key_index = data[i]
        value_index = data[i + 1]
        if isinstance(key_index, int) and isinstance(value_index, str):
            item = {"key": key_index, "value": value_index}
            result.append(item)
    return result
if __name__ == '__main__':
    sample_data = [0, 'a', 1, 'b', 2, 'c']
    structured_objects = transform_flat_list(sample_data)
    print(structured_objects)