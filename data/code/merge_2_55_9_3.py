def swap_adjacent(sequence):
    if not sequence:
        return []
    result = list(sequence)
    n = len(result)
    for i in range(0, n - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return result
if __name__ == '__main__':
    test_cases = [
        [],
        [42],
        [1, 2, 3, 4],
        ['a', 'b'],
        [5.5, 6.0, 7.7]
    ]
    for case in test_cases:
        print(f"Input: {case}")
        swapped = swap_adjacent(case)
        print(f"Output: {swapped}\n")