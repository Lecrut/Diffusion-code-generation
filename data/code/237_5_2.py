def find_pattern_sequence(sequence):
    n = len(sequence)
    if n < 2:
        return "None", sequence
    diffs = [sequence[i+1] - sequence[i] for i in range(n - 1)]
    ratios = []
    is_arithmetic = True
    is_geometric = True
    if n > 1:
        first_diff = diffs[0]
        for diff in diffs[1:]:
            if diff != first_diff:
                is_arithmetic = False
                break
        if is_arithmetic:
            return "Arithmetic", sequence
    for i in range(n - 1):
        if sequence[i] != 0:
            ratio = sequence[i+1] / sequence[i]
            ratios.append(ratio)
        elif sequence[i+1] != 0:
            is_geometric = False
            break
        else:
            pass
    if is_geometric and n > 1:
        first_ratio = None
        for ratio in ratios:
            if first_ratio is None:
                first_ratio = ratio
            elif abs(ratio - first_ratio) > 1e-9:
                is_geometric = False
                break
        if is_geometric:
            return "Geometric", sequence
    return "None", sequence
if __name__ == '__main__':
    sequence1 = [2, 4, 6, 8]
    print(f"Sequence: {sequence1}, Pattern: {find_pattern_sequence(sequence1)}")
    sequence2 = [3, 6, 9, 12]
    print(f"Sequence: {sequence2}, Pattern: {find_pattern_sequence(sequence2)}")
    sequence3 = [2, 4, 8, 16]
    print(f"Sequence: {sequence3}, Pattern: {find_pattern_sequence(sequence3)}")
    sequence4 = [1, 2, 4, 7]
    print(f"Sequence: {sequence4}, Pattern: {find_pattern_sequence(sequence4)}")
    sequence5 = [5, 10, 15, 20]
    print(f"Sequence: {sequence5}, Pattern: {find_pattern_sequence(sequence5)}")
    sequence6 = [1, 3, 7, 15]
    print(f"Sequence: {sequence6}, Pattern: {find_pattern_sequence(sequence6)}")
    sequence7 = [1, 2, 3, 4, 5]
    print(f"Sequence: {sequence7}, Pattern: {find_pattern_sequence(sequence7)}")
    sequence8 = [10, 5, 0, -5]
    print(f"Sequence: {sequence8}, Pattern: {find_pattern_sequence(sequence8)}")
    sequence9 = [2, 4, 6]
    print(f"Sequence: {sequence9}, Pattern: {find_pattern_sequence(sequence9)}")
    sequence10 = [5, 5, 5]
    print(f"Sequence: {sequence10}, Pattern: {find_pattern_sequence(sequence10)}")