def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    SAMPLE_LIST1 = [1, 2, 3, 4, 5]
    SAMPLE_LIST2 = [4, 5, 6, 7, 8]
    intersection_result = find_intersection(SAMPLE_LIST1, SAMPLE_LIST2)
    print(intersection_result)