def check_item_in_list_or_dict(item, container):
    if isinstance(container, list):
        return item in container
    elif isinstance(container, dict):
        for key, value in container.items():
            if key == item or value == item:
                return True
    else:
        raise TypeError("Container must be a list or dictionary.")
if __name__ == '__main__':
    sample_list = [10, 20, 'apple', None]
    sample_dict = {'a': 1, 'b': 2, 'c': 'apple'}
    test_item = 'apple'
    result_list = check_item_in_list_or_dict(test_item, sample_list)
    print(f"Item '{test_item}' found in list: {result_list}")
    result_dict = check_item_in_list_or_dict(test_item, sample_dict)
    print(f"Item '{test_item}' found in dictionary: {result_dict}")