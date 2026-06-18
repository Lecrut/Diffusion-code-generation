def transform_flat_list(data):
    if len(data) < 2:
        return []
    key_indices = [0]
    value_start_index = 1
    result_objects = []
    while value_start_index <= len(data):
        obj_data = {}
        if value_start_index < len(data):
            obj_data[data[value_start_index]] = None
            current_idx = value_start_index + 1
            while current_idx <= len(data):
                if isinstance(data[current_idx], str) and current_idx > value_start_index + 1:
                    obj_data[data[current_idx]] = data[value_start_index]
                    next_val_idx = current_idx + 2
                    if next_val_idx <= len(data):
                        val_candidate = data[next_val_idx]
                        pass
                current_idx += 1
        result_objects.append(obj_data)
    return []
def create_structured_objects(data):
    if not data or len(data) < 2:
        return []
    structured_list = []
    i = 1                                        
    while i <= len(data):
        key_idx = i - 1
        if isinstance(data[key_idx], str):
            obj = {}
            if i + 1 <= len(data):
                obj[data[key_idx]] = data[i+1]
                structured_list.append(obj)
                i += 2
        else:
            break
    return structured_list
if __name__ == '__main__':
    sample_data = ['id', 'A01', 'name', 'John', 'age', 30, 'city', 'NYC']
    result = []
    i = 1
    while i < len(sample_data):
        key_idx = i - 1
        if isinstance(sample_data[key_idx], str) or not isinstance(sample_data[i-1], int):
            obj = {}
            try:
                key_name = sample_data[key_idx]
                val_value = sample_data[i] if i < len(sample_data) else None
                obj[key_name] = val_value
                result.append(obj)
                i += 2
            except IndexError:
                break
        else:
            i += 1
    print(result)