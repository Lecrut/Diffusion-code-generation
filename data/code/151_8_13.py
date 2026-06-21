def merge_and_sort_lists(list1, list2):
    combined = set(list1 + list2)
    return sorted(combined)

if __name__ == '__main__':
    sample_list1 = [3.5, 4.2, 5.8]
    sample_list2 = [4.2, 6.0, 7.1]
    result = merge_and_sort_lists(sample_list1, sample_list2)
    print(result)