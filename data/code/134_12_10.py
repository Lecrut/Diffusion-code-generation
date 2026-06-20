def are_disjoint(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return len(intersection) == 0

if __name__ == '__main__':
    sample_list1 = [7, 8, 9]
    sample_list2 = [4, 5, 6]
    print(are_disjoint(sample_list1, sample_list2))