def get_middle_index(sequence):
    if not sequence:
        return -1
    length = len(sequence)
    half_length = (length + 1) >> 1
    return half_length
if __name__ == '__main__':
    test_cases = [
        [],
        ['a'],
        ['a', 'b'],
        ['a', 'b', 'c'],
        range(0, 10),
        list(range(5)) + list(range(-2, -6)),                                         
    ]
    for i, seq in enumerate(test_cases):
        result = get_middle_index(seq)
        print(f"Input: {seq} -> Middle Index: {result}")