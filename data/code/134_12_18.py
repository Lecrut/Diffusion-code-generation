def are_disjoint(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.isdisjoint(set2)
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    print(are_disjoint(sample_list1, sample_list2))