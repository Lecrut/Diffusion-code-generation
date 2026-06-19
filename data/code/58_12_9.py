def safe_first_element(iterable):
    try:
        return next(iter(iterable))
    except TypeError:
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3]
    SAMPLE_TUPLE = (4, 5, 6)
    SAMPLE_STRING = "hello"
    SAMPLE_DICT = {'a': 1, 'b': 2}
    SAMPLE_SET = {7, 8, 9}
    SAMPLE_EMPTY_LIST = []

    sample_values = [
        SAMPLE_LIST,
        SAMPLE_TUPLE,
        SAMPLE_STRING,
        SAMPLE_DICT,
        SAMPLE_SET,
        SAMPLE_EMPTY_LIST
    ]

    for value in sample_values:
        print(safe_first_element(value))