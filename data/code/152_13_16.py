def intersection(list1, list2):
    set1 = frozenset(list1)
    set2 = frozenset(list2)
    return list(set1 & set2)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [30, 40, 50, 60]
    result = intersection(sample_list1, sample_list2)
    print(f"Intersection of {sample_list1} and {sample_list2}: {result}")