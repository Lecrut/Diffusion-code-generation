def get_first_element(sequence):
    return sequence[0] if isinstance(sequence, (list, tuple)) and sequence else None

if __name__ == '__main__':
    SAMPLE_LIST = [25, 26, 27]
    SAMPLE_TUPLE = (28, 29, 30)
    EMPTY_LIST = []
    EMPTY_TUPLE = ()
    INVALID_INPUT = "not a sequence"
    
    print(get_first_element(SAMPLE_LIST))
    print(get_first_element(SAMPLE_TUPLE))
    print(get_first_element(EMPTY_LIST))
    print(get_first_element(EMPTY_TUPLE))
    print(get_first_element(INVALID_INPUT))