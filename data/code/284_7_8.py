def merge_and_reverse_lists(list1, list2):
    merged_list = list1 + list2
    reversed_list = []
    for item in merged_list:
        reversed_list.insert(0, item)
    return reversed_list
if __name__ == '__main__':
    sample_list1 = [5, 4, 3]
    sample_list2 = [2, 1]
    result = merge_and_reverse_lists(sample_list1, sample_list2)
    print(result)