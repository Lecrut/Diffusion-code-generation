def transform_flat_list(data):
    if len(data) < 2:
        return []
    key_indices = [0]
    value_start_index = 1
    result_objects = []
    for i in range(len(key_indices)):
        current_key_idx = key_indices[i]
        if i + 1 < len(key_indices):
            next_key_idx = key_indices[i + 1]
            value_end_index = next_key_idx - 1
        else:
            value_end_index = len(data) - 1
        obj_values = data[value_start_index:value_end_index+1]
        if isinstance(obj_values[0], str):
            try:
                attr_name, *rest = obj_values[:2]
                value_data = rest + [obj_values[-1]] if len(rest) > 0 else []
                structured_obj = {attr_name: value_data}
                result_objects.append(structured_obj)
            except (IndexError, ValueError):
                continue
        value_start_index += len(obj_values)
    return result_objects
if __name__ == '__main__':
    flat_list = ["id", "100", "type", "user", "role", "admin"]
    structured_data = transform_flat_list(flat_list)
    for item in structured_data:
        print(item)