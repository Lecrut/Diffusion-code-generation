def transform_flat_list(data):
    if len(data) < 2:
        return []
    key_index = 0
    value_indices = [1, 3]
    result_objects = []
    for i in range(0, len(data), 2):
        try:
            obj_key = data[i + key_index] if (i + key_index) < len(data) else None
            obj_value = data[i + value_indices[1]] if (i + value_indices[1]) < len(data) else None
            result_objects.append({
                "id": int(obj_key),
                "name": str(obj_value).strip()
            })
        except Exception:
            continue
    return result_objects
if __name__ == '__main__':
    flat_data = [1, 'Alice', 2, 'Bob', 3, 'Charlie']
    structured_result = transform_flat_list(flat_data)
    for item in structured_result:
        print(item)