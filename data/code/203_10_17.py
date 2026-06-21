def compare_lists(list1, list2):
    if not all((isinstance(x, int) for x in list1 + list2)):
        raise ValueError('Both lists must contain only integers.')
    len_list1 = len(list1)
    len_list2 = len(list2)
    min_len = min(len_list1, len_list2)
    for i in range(min_len):
        if list1[i] < list2[i]:
            return True
        elif list1[i] > list2[i]:
            return False
    return len_list1 < len_list2
if __name__ == '__main__':
    print(compare_lists([1, 2, 3], [4, 5, 6]))
    print(compare_lists([1, 2, 3], [1, 2, 2]))
    print(compare_lists([1, 2, 3], [1, 2]))