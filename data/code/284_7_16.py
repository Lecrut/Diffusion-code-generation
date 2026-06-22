def merge_and_reverse_lists(list1, list2):
    return list(reversed(list1 + list2))

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3]
    sample_list_2 = [4, 5, 6]
    result = merge_and_reverse_lists(sample_list_1, sample_list_2)
    print("Merged and reversed list:", result)