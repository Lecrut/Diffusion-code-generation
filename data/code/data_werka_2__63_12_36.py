def get_first_element(sequence):
    FIRST_ELEMENT_INDEX = 0
    try:
        return sequence[FIRST_ELEMENT_INDEX]
    except IndexError:
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [25, 26, 27]
    SAMPLE_TUPLE = (28, 29, 30)
    EMPTY_LIST = []
    EMPTY_TUPLE = ()
    
    print(get_first_element(SAMPLE_LIST))
    print(get_first_element(SAMPLE_TUPLE))
    print(get_first_element(EMPTY_LIST))
    print(get_first_element(EMPTY_TUPLE))