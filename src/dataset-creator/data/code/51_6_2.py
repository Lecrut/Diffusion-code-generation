def find_first_element(data_structure):
    if isinstance(data_structure, list):
        return data_structure[0] if len(data_structure) > 0 else None
    elif isinstance(data_structure, tuple):
        return data_structure[0] if len(data_structure) > 0 else None
    elif isinstance(data_structure, set):
        items = list(data_structure)
        return items[0] if len(items) > 0 else None
    elif isinstance(data_structure, dict):
        it = iter(data_structure.keys())
        try:
            next_key = next(it)
            return data_structure[next_key]
        except StopIteration:
            return None
    elif isinstance(data_structure, str):
        return data_structure[0] if len(data_structure) > 0 else None
    raise TypeError(f"Unsupported data structure type: {type(data_structure).__name__}")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('x', 'y')
    sample_set = {'b', 'a'}
    sample_dict = {'first': 42}
    sample_string = "Python"
    print(f"List first: {find_first_element(sample_list)}")
    print(f"Tuple first: {find_first_element(sample_tuple)}")
    print(f"Set first (arbitrary): {find_first_element(sample_set)}")
    print(f"Dict value of first key: {find_first_element(sample_dict)}")
    print(f"String char 0: {find_first_element(sample_string)}")
    try:
        find_first_element([])
    except TypeError as e:
        pass                                                                
    result_empty = find_first_element({})
    print(f"Empty set/ dict first (None): {result_empty}")
    invalid_input = [1, 2]
    try:
        find_first_element(invalid_input) 
    except TypeError as e:
        pass