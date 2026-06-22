def merge_and_reverse_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list[::-1]
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = merge_and_reverse_lists(sample_list1, sample_list2)
    print(result)