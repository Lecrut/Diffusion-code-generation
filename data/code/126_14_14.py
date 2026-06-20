def lists_are_equal(list1: list, list2: list) -> bool:
    return list1 == list2
if __name__ == '__main__':
    print(lists_are_equal([1, 2, 3], [1, 2, 3]))
    print(lists_are_equal([1, 2, 3], [3, 2, 1]))
    print(lists_are_equal([], []))
    print(lists_are_equal(['a', 'b'], ['a', 'b']))
    print(lists_are_equal(['a', 'b'], ['a', 'c']))