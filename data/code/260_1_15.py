INTERSECT_THRESHOLD = 0

def intersect_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    if len(intersection) >= INTERSECT_THRESHOLD:
        return sorted(list(intersection))
    else:
        return []
if __name__ == '__main__':
    sample_list_a = [1, 3, 5, 7]
    sample_list_b = [0, 2, 4, 6, 5]
    result = intersect_lists(sample_list_a, sample_list_b)
    print(result)
    sample_list_c = [10, 20, 30]
    sample_list_d = [15, 25, 35]
    result = intersect_lists(sample_list_c, sample_list_d)
    print(result)