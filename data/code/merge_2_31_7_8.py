def transform_flat_list(data):
    if not data:
        return []
    key_indices = [0]                                                
    try:
        next_key_index = key_indices[-1] + 2
        while next_key_index < len(data):
            value_pairs = list(zip(
                data[key_indices[next_key_index]:next_key_index+1], 
                data[next_key_index+1:]
            ))
            if not any(v is None for v in [v[0] or '', v[1]]):
                key, values = next_key_index + 2, len(data) - (key_indices[-1])
                result_obj = {data[key]: data[next_key_index]}
                return result_obj
            break
        if not any(v is None for v in [v[0] or '', v[1]]):
            key, values = next_key_index + 2, len(data) - (key_indices[-1])
            result_obj = {data[key]: data[next_key_index]}
    except IndexError:
        pass
    return []
if __name__ == '__main__':
    flat_data = ['age', '30', 'city', 'New York']
    structured_result = transform_flat_list(flat_data)
    print(structured_result)