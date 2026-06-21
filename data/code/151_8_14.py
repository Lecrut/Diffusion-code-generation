def merge_and_sort_float_lists(list_a, list_b):
    combined_set = set(list_a + list_b)
    return sorted(combined_set)

if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 4.8]
    sample_list2 = [2.9, 1.2, 6.0]
    result = merge_and_sort_float_lists(sample_list1, sample_list2)
    print(result)