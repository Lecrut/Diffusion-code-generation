def merge_lists(list1, list2):
    return [*list1, *list2]

if __name__ == '__main__':
    sample_list1 = [4, 5, 6]
    sample_list2 = ['x', 'y', 'z']
    merged_list = merge_lists(sample_list1, sample_list2)
    print(merged_list)