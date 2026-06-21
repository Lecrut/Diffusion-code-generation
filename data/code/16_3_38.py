def check_all_positive(numbers):
    POSITIVE_THRESHOLD = 0
    return all((num > POSITIVE_THRESHOLD for num in numbers))
if __name__ == '__main__':
    SAMPLE_VALUES_1 = [1, 2, 3, 4, 5]
    SAMPLE_VALUES_2 = [-1, -2, -3, -4, -5]
    SAMPLE_VALUES_3 = [0, 1, 2, 3, 4]
    print(check_all_positive(SAMPLE_VALUES_1))
    print(check_all_positive(SAMPLE_VALUES_2))
    print(check_all_positive(SAMPLE_VALUES_3))