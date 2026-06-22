def count_non_matching_elements(lst, data_type):
    return sum((not isinstance(x, data_type) for x in lst))
if __name__ == '__main__':
    sample_list = [1.0, True, 2, False]
    print(count_non_matching_elements(sample_list, float))