def find_middle_element(sequence):
    n = len(sequence)
    if n == 0:
        return None
    middle_index = n // 2
    return sequence[middle_index]

if __name__ == '__main__':
    SAMPLE_LIST_ODD = [1, 3, 5, 7, 9]
    SAMPLE_LIST_EVEN = [2, 4, 6, 8, 10, 12]
    SINGLE_ELEMENT_LIST = [42]
    EMPTY_LIST = []

    test_cases = [
        (SAMPLE_LIST_ODD, "odd"),
        (SAMPLE_LIST_EVEN, "even"),
        (SINGLE_ELEMENT_LIST, "single"),
        (EMPTY_LIST, "empty")
    ]

    for lst, description in test_cases:
        result = find_middle_element(lst)
        print(f"Middle element of {description} list: {result}")