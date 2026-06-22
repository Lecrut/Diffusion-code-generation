def find_middle_element(sequence):
    n = len(sequence)
    if n == 0:
        return None
    MIDDLE_INDEX = n // 2
    return sequence[MIDDLE_INDEX]

if __name__ == '__main__':
    SAMPLE_LIST_ODD = [7, 2, 9, 4, 3]
    SAMPLE_LIST_EVEN = [1, 6, 8, 5, 10, 12]
    SINGLE_ELEMENT_LIST = [42]
    EMPTY_LIST = []
    
    print(find_middle_element(SAMPLE_LIST_ODD))
    print(find_middle_element(SAMPLE_LIST_EVEN))
    print(find_middle_element(SINGLE_ELEMENT_LIST))
    print(find_middle_element(EMPTY_LIST))