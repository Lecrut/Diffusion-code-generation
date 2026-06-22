def merge_and_reverse_lists(list1, list2):
    merged_list = list1 + list2
    reversed_list = merged_list[::-1]
    return reversed_list

if __name__ == '__main__':
    sample_list1 = [5, 4, 3, 2, 1]
    sample_list2 = [6, 7, 8, 9, 10]
    result = merge_and_reverse_lists(sample_list1, sample_list2)
    print("Merged and reversed list:", result)