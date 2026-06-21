def lists_identical(lst1, lst2):
    return set(lst1) == set(lst2)
if __name__ == '__main__':
    print(lists_identical([1, 2, 3], [3, 2, 1]))
    print(lists_identical([1, 2, 3], [4, 5, 6]))