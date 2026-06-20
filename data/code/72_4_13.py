def merge_lists_by_index(list1, list2, index):
    return [(list1[index], list2[index])]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    sample_index = 1
    print(merge_lists_by_index(sample_list1, sample_list2, sample_index))