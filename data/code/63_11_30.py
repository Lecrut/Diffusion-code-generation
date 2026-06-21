def get_first_item(iterable):
    try:
        return next(iter(iterable))
    except StopIteration:
        raise ValueError('The iterable is empty')

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4]
    SAMPLE_TUPLE = (5, 6, 7, 8)
    SAMPLE_STRING = 'hello'
    SAMPLE_SET = {9, 10, 11}
    
    print(get_first_item(SAMPLE_LIST))
    print(get_first_item(SAMPLE_TUPLE))
    print(get_first_item(SAMPLE_STRING))
    print(get_first_item(SAMPLE_SET))