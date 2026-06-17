def get_middle_index(sequence):
    if not sequence:
        return -1
    n = len(sequence)
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2
if __name__ == '__main__':
    test_cases = [
        ([10], -1),
        ([], -1),
        ([1, 2], 1),
        ([1, 2, 3], 1),
        (range(5), 2)
    ]
    for seq in range(len(test_cases)):
        input_seq = test_cases[seq][0] if isinstance(test_cases[seq][0], list) else [test_cases[seq][0]]
        expected = test_cases[seq][1]
        result = get_middle_index(input_seq)
        print(f"Input: {input_seq}, Expected Index: {expected}, Result: {result}")