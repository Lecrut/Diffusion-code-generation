def absolute_difference_generator(list1, list2):
    LIST_LENGTH_MISMATCH_ERROR = "Both lists must have the same length."
    if len(list1) != len(list2):
        raise ValueError(LIST_LENGTH_MISMATCH_ERROR)
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    SAMPLE_LIST1 = [8, 16, 24, 32]
    SAMPLE_LIST2 = [1, 2, 3, 4]
    try:
        for diff in absolute_difference_generator(SAMPLE_LIST1, SAMPLE_LIST2):
            print(diff)
    except ValueError as e:
        print(e)