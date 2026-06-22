def reverse_merge_lists(list1, list2):
    return list1[::-1] + list2[::-1]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    result = reverse_merge_lists(sample_list1, sample_list2)
    print(result)