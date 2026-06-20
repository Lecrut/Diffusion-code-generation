def are_disjoint(list1, list2):
    set1 = set(list1)
    return not any(item in set2 for item in set1)

if __name__ == '__main__':
    print(are_disjoint([1, 2, 3], [4, 5, 6]))
    print(are_disjoint([1, 2, 3], [3, 4, 5]))