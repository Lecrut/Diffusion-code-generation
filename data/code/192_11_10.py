INTERSECTION_THRESHOLD = 0.5

def find_intersection(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    intersection = set_a.intersection(set_b)
    return list(intersection)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 2, 5]
    sample_list2 = [4, 5, 6, 2, 1]
    result = find_intersection(sample_list1, sample_list2)
    print(result)