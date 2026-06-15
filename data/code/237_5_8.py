def find_pattern_sequence(sequence):
    n = len(sequence)
    if n < 2:
        return "None", sequence
    diffs = [sequence[i+1] - sequence[i] for i in range(n - 1)]
    ratios = []
    is_arithmetic = True
    is_geometric = True
    if all(d == diffs[0] for d in diffs):
        return "Arithmetic", sequence
    for i in range(n - 1):
        if sequence[i] != 0:
            ratio = sequence[i+1] / sequence[i]
            ratios.append(ratio)
        else:
            ratios.append(float('inf') if sequence[i+1] != 0 else float('nan'))
    if len(ratios) > 0:
        first_ratio = ratios[0]
        is_geometric = True
        for i in range(1, len(ratios)):
            current_ratio = ratios[i]
            if not (abs(current_ratio - first_ratio) < 1e-9):
                is_geometric = False
                break
    if is_geometric:
        return "Geometric", sequence
    else:
        return "None", sequence
if __name__ == '__main__':
    sequence1 = [2, 4, 6, 8]
    print(f"Sequence: {sequence1}, Pattern: {find_pattern_sequence(sequence1)}")
    sequence2 = [3, 6, 12, 24]
    print(f"Sequence: {sequence2}, Pattern: {find_pattern_sequence(sequence2)}")
    sequence3 = [1, 2, 4, 8]
    print(f"Sequence: {sequence3}, Pattern: {find_pattern_sequence(sequence3)}")
    sequence4 = [1, 3, 5, 7]
    print(f"Sequence: {sequence4}, Pattern: {find_pattern_sequence(sequence4)}")
    sequence5 = [1, 2, 3, 5]
    print(f"Sequence: {sequence5}, Pattern: {find_pattern_sequence(sequence5)}")
    sequence6 = [10, 5, 0, -5]
    print(f"Sequence: {sequence6}, Pattern: {find_pattern_sequence(sequence6)}")
    sequence7 = [5, 5, 5, 5]
    print(f"Sequence: {sequence7}, Pattern: {find_pattern_sequence(sequence7)}")