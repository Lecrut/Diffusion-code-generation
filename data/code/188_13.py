def reverse_list(iterable):
    return list(reversed(iterable))
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(f"Original: {list1}")
    print(f"Reversed: {reverse_list(list1)}")
    list2 = ['a', 'b', 'c']
    print(f"Original: {list2}")
    print(f"Reversed: {reverse_list(list2)}")
    empty_list = []
    print(f"Original: {empty_list}")
    print(f"Reversed: {reverse_list(empty_list)}")
    list3 = [10]
    print(f"Original: {list3}")
    print(f"Reversed: {reverse_list(list3)}")