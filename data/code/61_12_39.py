def get_element(sequence, index):
    if not hasattr(sequence, '__getitem__'):
        raise ValueError('Invalid sequence type')
    try:
        return sequence[index]
    except IndexError:
        raise ValueError('Index out of range')
if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    SAMPLE_TUPLE = (100, 200, 300, 400, 500)
    SAMPLE_STRING = 'Hello, World!'
    print(get_element(SAMPLE_LIST, 2))
    print(get_element(SAMPLE_TUPLE, 3))
    print(get_element(SAMPLE_STRING, 7))
    try:
        print(get_element(SAMPLE_LIST, 10))
    except ValueError as e:
        print(e)
    try:
        print(get_element(12345, 1))
    except ValueError as e:
        print(e)