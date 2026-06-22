def fetch_first_element(sequence):
    try:
        return sequence[0]
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [7, 8, 9]
    SAMPLE_TUPLE = (10, 11, 12)
    EMPTY_LIST = []
    EMPTY_TUPLE = ()
    NON_SEQUENCE = "not a sequence"
    
    test_cases = [
        SAMPLE_LIST,
        SAMPLE_TUPLE,
        EMPTY_LIST,
        EMPTY_TUPLE,
        NON_SEQUENCE
    ]
    
    for case in test_cases:
        print(fetch_first_element(case))