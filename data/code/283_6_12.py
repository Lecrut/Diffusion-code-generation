def count_non_dict_elements(lst):
    non_dict_count = sum((1 for item in lst if not isinstance(item, dict)))
    return non_dict_count
if __name__ == '__main__':
    sample_list = [1, 2, {'a': 3}, 'b', {}, [], (1, 2)]
    result = count_non_dict_elements(sample_list)
    print(result)