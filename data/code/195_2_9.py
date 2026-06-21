def is_subset(list1, list2):
    return set(list1) <= set(list2)

if __name__ == '__main__':
    print(is_subset([1, 2, 3], [4, 5, 6, 7, 1, 2, 3]))
    print(is_subset([1, 2, 3], [1, 2, 4]))