def reverse_list(iterable):
    return list(reversed(iterable))
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(f"Original: {list1}, Reversed: {reverse_list(list1)}")
    list2 = ['a', 'b', 'c']
    print(f"Original: {list2}, Reversed: {reverse_list(list2)}")
    empty_list = []
    print(f"Original: {empty_list}, Reversed: {reverse_list(empty_list)}")
    list3 = [10, 20]
    print(f"Original: {list3}, Reversed: {reverse_list(list3)}")