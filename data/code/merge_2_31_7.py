def transform_flat_list(data):
    if len(data) < 2:
        return []
    key_index = data[0]
    value_indices = [i for i in range(1, len(data)) if isinstance(i, int)]
    result_objects = []
    current_key = None
    if isinstance(data[0], str):
        result_objects.append({"name": data[0]})
    for i in range(2, len(data), 2):
        if i + 1 < len(data):
            key = f"key_{i-1}"
            value = data[i+1]
            obj = {key: value}
            result_objects.append(obj)
    return result_objects
if __name__ == '__main__':
    flat_data = ["age", 25, "city", "New York", "country", "USA"]
    structured_result = transform_flat_list(flat_data)
    for item in structured_result:
        print(item)