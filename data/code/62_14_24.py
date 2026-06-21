def retrieve_second_element(sequence):
    MIN_LENGTH = 2
    if len(sequence) < MIN_LENGTH:
        return None
    return sequence[1]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4],
        ['x', 'y'],
        [True, False, True],
        [],
        [42]
    ]
    
    for index, case in enumerate(test_cases):
        result = retrieve_second_element(case)
        print(f"Test Case {index + 1}: {result}")