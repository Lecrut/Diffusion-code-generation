def values_differ(a, b):
    return not (a == b)

if __name__ == '__main__':
    SAMPLE_INT1 = 10
    SAMPLE_INT2 = 20
    SAMPLE_STR1 = 'hello'
    SAMPLE_STR2 = 'world'
    SAMPLE_LIST1 = [1, 2]
    SAMPLE_LIST2 = [1, 2, 3]
    SAMPLE_DICT1 = {'a': 1}
    SAMPLE_DICT2 = {'a': 1}

    print(values_differ(SAMPLE_INT1, SAMPLE_INT2))
    print(values_differ(SAMPLE_STR1, SAMPLE_STR2))
    print(values_differ(SAMPLE_LIST1, SAMPLE_LIST2))
    print(values_differ(SAMPLE_DICT1, SAMPLE_DICT2))