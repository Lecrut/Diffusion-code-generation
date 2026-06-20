def lists_equal(list1: list, list2: list) -> bool:
    return list1 == list2

if __name__ == '__main__':
    print(lists_equal([1, 2, 3], [1, 2, 3]))
    print(lists_equal([1, 2, 3], [3, 2, 1]))
    print(lists_equal([], []))
    print(lists_equal(['a', 'b'], ['a', 'b', 'c']))