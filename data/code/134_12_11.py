def are_disjoint(list1, list2):
    set2 = set(list2)
    for item in list1:
        if item in set2:
            return False
    return True

if __name__ == '__main__':
    print(are_disjoint([1, 2, 3], [4, 5, 6]))
    print(are_disjoint([1, 2, 3], [3, 4, 5]))