def find_first_element(data_structure):
    if isinstance(data_structure, list):
        return data_structure[0] if len(data_structure) > 0 else None
    elif isinstance(data_structure, tuple):
        return data_structure[0] if len(data_structure) > 0 else None
    elif isinstance(data_structure, set):
        for item in data_structure:
            return item
    elif isinstance(data_structure, dict):
        first_key = next(iter(data_structure))
        return data_structure[first_key]
    elif isinstance(data_structure, str):
        if len(data_structure) > 0:
            return data_structure[0]
    else:
        raise TypeError(f"Unsupported data structure type: {type(data_structure).__name__}")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (5, 'text', True)
    sample_set = {7, 8, 9}
    sample_dict = {'alpha': 'beta'}
    sample_string = "Advanced"
    print(f"First in list: {find_first_element(sample_list)}")
    print(f"First in tuple: {find_first_element(sample_tuple)}")
    first_set_item = find_first_element(sample_set)
    if isinstance(first_set_item, int):
        print(f"First set item (int check): {first_set_item}")
    print(f"First dict value: {find_first_element(sample_dict)}")
    print(f"First string char: {find_first_element(sample_string)}")