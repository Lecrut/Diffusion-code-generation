def calculate_difference_sum(list1, list2):
    MIN_LENGTH = min(len(list1), len(list2))
    difference_sum = 0
    for index in range(MIN_LENGTH):
        difference_sum += list1[index] - list2[index]
    return difference_sum

if __name__ == '__main__':
    SAMPLE_LIST_A = [8, 6, 4, 2, 0]
    SAMPLE_LIST_B = [1, 3, 5, 7, 9]
    result = calculate_difference_sum(SAMPLE_LIST_A, SAMPLE_LIST_B)
    print(result)