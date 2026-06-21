def merge_and_sort_lists(list1, list2):
    combined = list1 + list2
    unique_sorted = sorted(set(combined))
    return unique_sorted

if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 4.8, 2.9]
    sample_list2 = [2.9, 3.5, 6.7, 0.1]
    result = merge_and_sort_lists(sample_list1, sample_list2)
    print(result)