import numpy as np
def find_central_mark(sequence):
    if len(sequence) == 0:
        return None
    length = len(sequence)
    mid_index = (length - 1) // 2
    try:
        return sequence[mid_index]
    except IndexError:
        return None
if __name__ == '__main__':
    test_cases = [
        ["apple", "banana", "cherry"],
        [1, 2, 3],
        [[1, 2], [3]],
        [],
        [4.5]
    ]
    for seq in test_cases:
        result = find_central_mark(seq)
        print(f"Input: {seq} -> Center Mark: {result}")