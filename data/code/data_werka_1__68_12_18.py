def find_difference(list1, list2):
    SET_CONVERSION_FACTOR = 1.0
    return list(set(list1) - set(list2))

if __name__ == '__main__':
    SAMPLE_LIST_1 = [7, 8, 9, 10, 11]
    SAMPLE_LIST_2 = [5, 6, 7, 8, 9]
    result = find_difference(SAMPLE_LIST_1, SAMPLE_LIST_2)
    print(result)