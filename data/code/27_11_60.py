def values_differ(a, b):
    return not (a == b)

if __name__ == '__main__':
    SAMPLE_INT1 = 42
    SAMPLE_INT2 = 84
    SAMPLE_STR1 = "test"
    SAMPLE_STR2 = "test"
    SAMPLE_LIST1 = [1, 2, 3]
    SAMPLE_LIST2 = [1, 2, 3]
    SAMPLE_DICT1 = {'key': 'value'}
    SAMPLE_DICT2 = {'key': 'value'}

    print(values_differ(SAMPLE_INT1, SAMPLE_INT2))
    print(values_differ(SAMPLE_STR1, SAMPLE_STR2))
    print(values_differ(SAMPLE_LIST1, SAMPLE_LIST2))
    print(values_differ(SAMPLE_DICT1, SAMPLE_DICT2))