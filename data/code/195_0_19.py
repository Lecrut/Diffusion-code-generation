def lists_are_identical(list1, list2):
    return len(list1) == len(list2) and all((x == y for x, y in zip(list1, list2)))
if __name__ == '__main__':
    print(lists_are_identical([1, 2, 3], [1, 2, 3]))
    print(lists_are_identical([1, 2, 3], [1, 2, 4]))
    print(lists_are_identical([], []))
    print(lists_are_identical([], [1]))