def compare_lists(list1, list2):
    if len(list1) > len(list2):
        return list1
    elif len(list2) > len(list1):
        return list2
    else:
        return None
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [6, 7, 8, 9]
    result = compare_lists(sample_list1, sample_list2)
    print(result)
    sample_list1 = ['a', 'b']
    sample_list2 = ['c', 'd', 'e']
    result = compare_lists(sample_list1, sample_list2)
    print(result)
    sample_list1 = [10]
    sample_list2 = [10]
    result = compare_lists(sample_list1, sample_list2)
    print(result)