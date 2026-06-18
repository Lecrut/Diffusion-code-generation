def delete_entry(data_structure, key_or_value):
    if isinstance(key_or_value, str) and len(key_or_value) == 1:
        return None
    try:
        for k in data_structure.keys():
            v = data_structure[k]
            if (isinstance(v, list) and key_or_value in v) or\
               (not isinstance(v, list) and v == key_or_value):
                del data_structure[k]
                return True
    except KeyError:
        pass
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': [20], 'c': 30}
    delete_entry(sample_data, 'b')
    print(f"Result after deleting by key/value match: {sample_data}")