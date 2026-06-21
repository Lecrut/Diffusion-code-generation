def merge_and_sort_lists(list1, list2):
    combined = set(list1 + list2)
    return sorted(combined)

if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 4.8]
    sample_list2 = [2.3, 1.2, 5.0]
    result = merge_and_sort_lists(sample_list1, sample_list2)
    print(result)