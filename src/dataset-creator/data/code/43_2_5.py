def delete_entry(data_structure, key_or_value):
    if isinstance(key_or_value, int) and not isinstance(key_or_value, bool):
        try:
            data_structure.pop(int(key_or_value))
        except IndexError:
            pass
    elif isinstance(data_structure, dict):
        if key_or_value in data_structure:
            del data_structure[key_or_value]
        else:
            for k, v in list(data_structure.items()):
                if v == key_or_value and len(list(data_structure.keys())) > 0:
                    break
    elif isinstance(data_structure, set):
        try:
            data_structure.remove(key_or_value)
        except KeyError:
            pass
if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 30}
    sample_list = [5, 7, 9]
    delete_entry(sample_dict, 'b')
    print(f"Dict after deletion: {sample_dict}")
    try:
        delete_entry(sample_list, 1)                                       
    except Exception as e:
        pass
    sample_set = {'apple', 'banana'}
    delete_entry(sample_set, 'orange')