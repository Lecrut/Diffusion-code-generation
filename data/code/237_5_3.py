def find_pattern_sequence(sequence):
    n = len(sequence)
    if n <= 1:
        return "None", sequence
    diffs = [sequence[i+1] - sequence[i] for i in range(n - 1)]
    ratios = []
    for i in range(n - 1):
        if sequence[i] != 0:
            ratios.append(sequence[i+1] / sequence[i])
        else:
            ratios.append(None)
    is_arithmetic = True
    if n > 1:
        first_diff = diffs[0]
        for diff in diffs[1:]:
            if diff != first_diff:
                is_arithmetic = False
                break
    if is_arithmetic:
        return "Arithmetic", sequence
    is_geometric = True
    if n > 1:
        first_ratio = ratios[0]
        if first_ratio is None:
            is_geometric = False
        else:
            for ratio in ratios[1:]:
                if ratio is None:
                    is_geometric = False
                    break
                if abs(ratio - first_ratio) > 1e-9:
                    is_geometric = False
                    break
    if is_geometric:
        return "Geometric", sequence
    return "None", sequence
if __name__ == '__main__':
    sequence1 = [2, 4, 6, 8, 10]
    print(f"Sequence: {sequence1}, Pattern: {find_pattern_sequence(sequence1)}")
    sequence2 = [2, 4, 8, 16, 32]
    print(f"Sequence: {sequence2}, Pattern: {find_pattern_sequence(sequence2)}")
    sequence3 = [1, 3, 5, 7, 9]
    print(f"Sequence: {sequence3}, Pattern: {find_pattern_sequence(sequence3)}")
    sequence4 = [1, 2, 4, 8, 16]
    print(f"Sequence: {sequence4}, Pattern: {find_pattern_sequence(sequence4)}")
    sequence5 = [1, 2, 3, 4, 5]
    print(f"Sequence: {sequence5}, Pattern: {find_pattern_sequence(sequence5)}")
    sequence6 = [1, 2, 3, 5, 7]
    print(f"Sequence: {sequence6}, Pattern: {find_pattern_sequence(sequence6)}")
    sequence7 = [10, 8, 6, 4, 2]
    print(f"Sequence: {sequence7}, Pattern: {find_pattern_sequence(sequence7)}")
    sequence8 = [5, 10, 15, 22, 29]
    print(f"Sequence: {sequence8}, Pattern: {find_pattern_sequence(sequence8)}")