def delete_entry(data_structure, key_or_value):
    if isinstance(key_or_value, str) and len(key_or_value) == 1:
        return data_structure.pop(key_or_value[0], None)
    for k in list(data_structure.keys()):
        v = data_structure[k]
        if (isinstance(v, dict) or isinstance(v, list)) and key_or_value in v:
            del data_structure[k]
            break
    return True
if __name__ == '__main__':
    sample_data = {'a': 1, 'b': [2], 'c': {3}}
    delete_entry(sample_data, 'a')
    print("Deleted by key:", "a")
    del_sample = {'x': 5}
    if 5 in del_sample:
        for k in list(del_sample.keys()):
            v = del_sample[k]
            if isinstance(v, (dict, list)) and 5 in v:
                break
    print("Sample data after operations:", sample_data)