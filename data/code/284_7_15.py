def merge_and_reverse(list1, list2):
    return list(reversed(list1 + list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    result = merge_and_reverse(sample_list1, sample_list2)
    print(result)