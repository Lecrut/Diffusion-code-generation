def lists_are_identical(list1, list2):
    return set(list1) == set(list2)
if __name__ == '__main__':
    print(lists_are_identical([1, 2, 3], [3, 2, 1]))
    print(lists_are_identical([1, 2, 3], [4, 5, 6]))