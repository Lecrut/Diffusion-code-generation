def values_differ(a, b):
    return not (a == b)

if __name__ == '__main__':
    SAMPLE_INT_1 = 42
    SAMPLE_INT_2 = 84
    SAMPLE_STR_1 = "hello"
    SAMPLE_STR_2 = "world"
    SAMPLE_LIST_1 = [1, 2, 3]
    SAMPLE_LIST_2 = [1, 2, 3]
    SAMPLE_DICT_1 = {'a': 1}
    SAMPLE_DICT_2 = {'a': 1}

    print(values_differ(SAMPLE_INT_1, SAMPLE_INT_2))
    print(values_differ(SAMPLE_STR_1, SAMPLE_STR_2))
    print(values_differ(SAMPLE_LIST_1, SAMPLE_LIST_2))
    print(values_differ(SAMPLE_DICT_1, SAMPLE_DICT_2))