def transform_flat_list(data):
    if len(data) < 2:
        return []
    key_index = data[0]
    value_indices = [i for i in range(1, len(data)) if isinstance(i, int)]
    result_objects = []
    current_key = None
    if isinstance(data[0], int):
        start_index = data[0] + 1
        for i in range(start_index, len(data), 2):
            current_key = data[i - 1]
            result_objects.append({current_key: data[i]})
    return result_objects
if __name__ == '__main__':
    flat_data = [0, 'id_1', 'val_a', 'id_2', 'val_b']
    structured_result = transform_flat_list(flat_data)
    print(structured_result)