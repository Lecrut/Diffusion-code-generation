def transform_flat_list(data):
    if len(data) < 2:
        return []
    result = []
    for i in range(0, len(data), 2):
        key = data[i]
        value = data[i + 1]
        result.append({"key": key, "value": value})
    return result
if __name__ == '__main__':
    flat_data = ["id_1", "Alice", "id_2", "Bob", "id_3", None]
    structured_objects = transform_flat_list(flat_data)
    for obj in structured_objects:
        print(obj)