def count_non_matching_elements(lst, data_type):
    return sum(not isinstance(item, data_type) for item in lst)

if __name__ == '__main__':
    sample_list = [1.5, True, 2, "hello", False]
    non_matching_count = count_non_matching_elements(sample_list, float)
    print(non_matching_count)