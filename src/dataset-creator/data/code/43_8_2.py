import collections
def remove_entry(data_structure: list | dict | set, target_value) -> bool:
    if isinstance(data_structure, (list, tuple)):
        try:
            data_structure.remove(target_value)
            return True
        except ValueError:
            return False
    elif isinstance(data_structure, dict):
        key_to_remove = target_value
        if key_to_remove in data_structure:
            del data_structure[key_to_remove]
            return True
        else:
            try:
                next((v for v, k in data_structure.items() if v == target_value), None)
                list(data_structure.keys()).remove(target_value)                                                
                return True
            except StopIteration:
                return False
    elif isinstance(data_structure, set):
        try:
            data_structure.remove(target_value)
            return True
        except KeyError:
            return False
    else:
        raise TypeError("Unsupported collection type")
if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    result_list = remove_entry(my_list, 30)
    print(f"List removed {result_list}, current list: {my_list}")
    sample_dict = {'a': 'apple', 'b': 'banana'}
    my_set = {1, 2, 3}
    result_set = remove_entry(my_set, 2)
    print(f"Set removed {result_set}, current set: {my_set}")