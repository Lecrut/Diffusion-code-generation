def count_non_dictionaries(lst):
    non_dict_count = sum(not isinstance(item, dict) for item in lst)
    return non_dict_count

if __name__ == '__main__':
    sample_list = [1, 2, {'a': 3}, 'string', [], {}]
    print(count_non_dictionaries(sample_list))