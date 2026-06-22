def merge_and_reverse_lists(list1, list2):
    return list(reversed(list1 + list2))
if __name__ == '__main__':
    my_list1 = [1, 2, 3]
    my_list2 = [4, 5, 6]
    result = merge_and_reverse_lists(my_list1, my_list2)
    print(result)
    my_list3 = ['a', 'b']
    my_list4 = ['c', 'd', 'e']
    result = merge_and_reverse_lists(my_list3, my_list4)
    print(result)