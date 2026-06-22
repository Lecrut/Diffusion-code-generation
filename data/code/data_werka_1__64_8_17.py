def find_last_greater_equal(data, threshold):
    n = len(data)
    result = -1
    index = n - 1
    while index >= 0:
        if data[index] >= threshold:
            result = index
            break
        index -= 1
    return result

if __name__ == '__main__':
    SAMPLE_LIST_1 = [10, 5, 20, 15, 30, 25]
    THRESHOLD_1 = 20
    print(find_last_greater_equal(SAMPLE_LIST_1, THRESHOLD_1))

    SAMPLE_LIST_2 = [3, 1, 4, 1, 5, 9, 2, 6]
    THRESHOLD_2 = 5
    print(find_last_greater_equal(SAMPLE_LIST_2, THRESHOLD_2))

    SAMPLE_LIST_3 = [1, 2, 3, 4, 5]
    THRESHOLD_3 = 6
    print(find_last_greater_equal(SAMPLE_LIST_3, THRESHOLD_3))