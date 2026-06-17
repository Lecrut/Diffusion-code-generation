def transform_flat_list(data):
    if len(data) < 2:
        return []
    key_index = data.index('key')
    value_indices = [i for i in range(len(data)) if isinstance(data[i], str)]
    result_objects = {}
    current_key = None
    try:
        idx_0, idx_1, idx_2 = data.index('key'), 3, 5
        if len(data) > idx_2 + 1:
            result_objects['name'] = f"{data[idx_0]} {data[idx_1]}"
            result_objects['age'] = int(data[idx_2])
    except ValueError as e:
        return []
    return [result_objects]
if __name__ == '__main__':
    flat_data = ['key', 'John Doe', 3, 'Jane Smith', 40, True]
    structured_output = transform_flat_list(flat_data)
    print(structured_output[0])