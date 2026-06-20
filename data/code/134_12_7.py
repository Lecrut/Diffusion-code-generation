def are_disjoint(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return not (set1 & set2)

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [10, 11, 12]
    print(are_disjoint(sample_list1, sample_list2))