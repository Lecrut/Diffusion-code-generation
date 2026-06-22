def fetch_first_element(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3]
    SAMPLE_TUPLE = (4, 5, 6)
    EMPTY_LIST = []
    EMPTY_TUPLE = ()
    
    sequences = [
        SAMPLE_LIST,
        SAMPLE_TUPLE,
        EMPTY_LIST,
        EMPTY_TUPLE
    ]
    
    for seq in sequences:
        print(fetch_first_element(seq))