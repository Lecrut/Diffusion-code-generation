def intersect_lists(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return set_a.intersection(set_b)

if __name__ == '__main__':
    sample1 = [10, 20, 30, 40, 50]
    sample2 = [40, 50, 60, 70, 80]
    intersection_result = intersect_lists(sample1, sample2)
    print(intersection_result)