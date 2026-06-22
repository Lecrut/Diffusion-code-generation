def get_element(sequence, index):
    try:
        return sequence[index]
    except IndexError as e:
        raise ValueError('Index out of range') from e
    except TypeError as e:
        raise ValueError('Invalid sequence type') from e

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    SAMPLE_TUPLE = (100, 200, 300, 400, 500)
    
    print(get_element(SAMPLE_LIST, 2))
    print(get_element(SAMPLE_TUPLE, 3))
    
    try:
        print(get_element(SAMPLE_LIST, 10))
    except ValueError as e:
        print(e)
    
    try:
        print(get_element(12345, 1))
    except ValueError as e:
        print(e)