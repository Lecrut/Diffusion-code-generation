def are_disjoint(list1, list2):
    set1 = set(list1)
    return len(set1.intersection(list2)) == 0

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [5, 6, 7, 8]
    print(are_disjoint(sample_list1, sample_list2))