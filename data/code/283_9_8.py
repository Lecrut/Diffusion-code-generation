def count_non_matching_elements(lst, data_type):
    return sum(not isinstance(item, data_type) for item in lst)

if __name__ == '__main__':
    sample_list = [3.14, True, 'hello', 2, False]
    non_matching_count = count_non_matching_elements(sample_list, float)
    print(non_matching_count)