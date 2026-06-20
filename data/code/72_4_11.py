def merge_lists_at_index(list1, list2, index):
    return [(list1[index], list2[index])]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = ['x', 'y', 'z']
    sample_index = 1
    print(merge_lists_at_index(sample_list1, sample_list2, sample_index))