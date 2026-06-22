def get_first_item(iterable):
    EMPTY_ITERABLE_MESSAGE = 'The iterable is empty'
    if not iterable:
        raise ValueError(EMPTY_ITERABLE_MESSAGE)
    return next(iter(iterable))

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30]
    SAMPLE_TUPLE = (40, 50, 60)
    SAMPLE_STRING = 'example'
    SAMPLE_SET = {70, 80, 90}

    print(get_first_item(SAMPLE_LIST))
    print(get_first_item(SAMPLE_TUPLE))
    print(get_first_item(SAMPLE_STRING))
    print(get_first_item(SAMPLE_SET))