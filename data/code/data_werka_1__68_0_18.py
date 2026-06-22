def calculate_difference_sum(list1, list2):
    MIN_LENGTH = min(len(list1), len(list2))
    difference_sum = 0
    for i in range(MIN_LENGTH):
        difference_sum += list1[i] - list2[i]
    return difference_sum

if __name__ == '__main__':
    SAMPLE_LIST_A = [1, 2, 3, 4, 5]
    SAMPLE_LIST_B = [10, 20, 30, 40]
    result = calculate_difference_sum(SAMPLE_LIST_A, SAMPLE_LIST_B)
    print(result)