def swap_adjacent(values):
    if not isinstance(values, (list, tuple)):
        return "Input must be a list or tuple."
    result = []
    for i in range(0, len(values), 2):
        if i + 1 < len(values):
            result.extend([values[i], values[i+1]])
        else:
            result.append(values[i])
    return result
if __name__ == '__main__':
    test_cases = [
        [],
        [42],
        [1, 2, 3],
        ['a', 'b'],
        [5.0, 6.0]
    ]
    for case in test_cases:
        print(f"Input: {case} -> Output: {swap_adjacent(case)}")