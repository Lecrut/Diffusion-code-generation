def find_intersection(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = set_a.intersection(set_b)
    return list(intersection)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50, 60]
    sample_list2 = [50, 60, 70, 80, 90, 10]
    result = find_intersection(sample_list1, sample_list2)
    print(result)