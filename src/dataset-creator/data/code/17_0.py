def check_list_item(item, data):
    if not isinstance(data, list) and not isinstance(data, dict):
        raise TypeError("Data must be a list or dictionary.")
    try:
        return item in data
    except TypeError as e:
        raise RuntimeError(f"Item type mismatch for {type(item).__name__}: {e}")
if __name__ == '__main__':
    sample_list = [1, 2, 'apple', None]
    sample_dict = {'a': 10, 'b': 20}
    list_check_result = check_list_item(3, sample_list)
    dict_check_result = check_list_item('c', sample_dict)
    print(f"List item found: {list_check_result}")
    print(f"Dict key found: {dict_check_result}")