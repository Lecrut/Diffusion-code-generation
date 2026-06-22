def find_difference(list1, list2):
    SET_CONVERSION_FACTOR = 1.0
    THRESHOLD = 0

    set1 = set(list1)
    set2 = set(list2)

    difference_set = set1.difference(set2)
    return list(difference_set)

if __name__ == '__main__':
    SAMPLE_LIST_1 = [5, 15, 25, 35, 45]
    SAMPLE_LIST_2 = [10, 20, 30, 40, 50]

    result = find_difference(SAMPLE_LIST_1, SAMPLE_LIST_2)
    print(result)