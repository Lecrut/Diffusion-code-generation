def find_middle_element(sequence):
    if not sequence:
        return None
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40, 50, 60],
        [1, 2, 3, 4],
        [100],
        []
    ]
    for i, lst in enumerate(test_cases):
        result = find_middle_element(lst)
        print(f"Test case {i+1}: Middle element of {lst} is {result}")