def merge_lists_at_index(list1, list2, index):
    if len(list1) > index and len(list2) > index:
        return [(list1[index], list2[index])]
    else:
        return []

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = ['x', 'y', 'z']
    sample_index = 1
    result = merge_lists_at_index(sample_list1, sample_list2, sample_index)
    print(result)