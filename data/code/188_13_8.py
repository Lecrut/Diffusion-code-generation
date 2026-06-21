def reverse_list(lst):
    return lst[::-1]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(f"Original: {list1}, Reversed: {reverse_list(list1)}")
    list2 = ['a', 'b', 'c']
    print(f"Original: {list2}, Reversed: {reverse_list(list2)}")
    empty_list = []
    print(f"Original: {empty_list}, Reversed: {reverse_list(empty_list)}")
    single_element_list = [10]
    print(f"Original: {single_element_list}, Reversed: {reverse_list(single_element_list)}")