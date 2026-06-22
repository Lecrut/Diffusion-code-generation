def count_non_dictionaries(data):
    non_dict_count = sum(not isinstance(x, dict) for x in data)
    return non_dict_count

if __name__ == '__main__':
    sample_list1 = [1, 5, {'a': 2}, 'string']
    sample_list2 = [{'b': 3}, {'c': 4}]
    sample_list3 = [True, False, None]
    
    print(f"Sample List 1: {count_non_dictionaries(sample_list1)}")
    print(f"Sample List 2: {count_non_dictionaries(sample_list2)}")
    print(f"Sample List 3: {count_non_dictionaries(sample_list3)}")