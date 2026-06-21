def are_equal(a, b):
    return a == b

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 2, 3]
    SAMPLE_LIST_2 = [1, 2, 4]
    SAMPLE_DICT_1 = {"a": 1}
    SAMPLE_DICT_2 = {"a": 1}
    print(are_equal(SAMPLE_LIST_1, SAMPLE_LIST_1))  # True
    print(are_equal(SAMPLE_LIST_1, SAMPLE_LIST_2))  # False
    print(are_equal(SAMPLE_DICT_1, SAMPLE_DICT_1))  # True
    print(are_equal(SAMPLE_DICT_1, {"a": 2}))     # False