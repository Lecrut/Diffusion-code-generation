def compute_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    return sorted(intersection)

if __name__ == '__main__':
    sample_list1 = [4, 2, 9, 3, 5, 1]
    sample_list2 = [8, 3, 1, 7, 4, 2]
    result = compute_intersection(sample_list1, sample_list2)
    print(result)