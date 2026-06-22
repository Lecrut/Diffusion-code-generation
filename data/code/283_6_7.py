def count_non_dict_elements(input_list):
    non_dict_count = sum(not isinstance(item, dict) for item in input_list)
    return non_dict_count

if __name__ == '__main__':
    sample_list = [1, 2, {'a': 3}, 'hello', [], {}, None]
    print(count_non_dict_elements(sample_list))