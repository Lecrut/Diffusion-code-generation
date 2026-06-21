def get_middle_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    return sequence[length // 2 - 1]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [1, 2, 3, 4],
        [],
        [10],
        ['a', 'b', 'c', 'd', 'e']
    ]
    for case in test_cases:
        result = get_middle_item(case)
        print(f"Sequence: {case} -> Middle: {result}")