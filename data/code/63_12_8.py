def get_first_item(iterable):
    return next(iter(iterable), None)

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40]
    SAMPLE_TUPLE = (5, 15, 25)
    SAMPLE_STRING = "Hello World"
    EMPTY_LIST = []

    print(get_first_item(SAMPLE_LIST))
    print(get_first_item(SAMPLE_TUPLE))
    print(get_first_item(SAMPLE_STRING))
    print(get_first_item(EMPTY_LIST))