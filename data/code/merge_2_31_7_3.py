def transform_flat_list(data):
    if len(data) < 2:
        return []
    key_index = data[0]
    value_indices = [i for i in range(1, len(data)) if isinstance(i, int)]
    result_objects = []
    current_key = None
    if isinstance(data[0], str):
        result_objects.append({data[0]: data[1]})
    return result_objects
if __name__ == '__main__':
    sample_data = ["Name", "Alice"]
    transformed = transform_flat_list(sample_data)
    print(transformed)