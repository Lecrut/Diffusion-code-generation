def count_non_dict_elements(lst):
    return sum(not isinstance(item, dict) for item in lst)

if __name__ == '__main__':
    sample_list = [1, 2, {'a': 3}, 'string', [], {}]
    print(count_non_dict_elements(sample_list))