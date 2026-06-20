def are_disjoint(list1, list2):
    set1 = set(list1)
    return set1.isdisjoint(set2)
if __name__ == '__main__':
    print(are_disjoint([1, 2, 3], [4, 5, 6]))
    print(are_disjoint([1, 2, 3], [3, 4, 5]))