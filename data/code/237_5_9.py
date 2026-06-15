def find_pattern_sequence(sequence):
    n = len(sequence)
    if n < 2:
        return "None", sequence
    diffs = [sequence[i+1] - sequence[i] for i in range(n - 1)]
    ratios = []
    is_arithmetic = True
    is_geometric = True
    for i in range(n - 1):
        if sequence[i] == 0:
            if sequence[i+1] != 0:
                is_geometric = False
            else:
                ratios.append(1.0)                                                                                                         
        else:
            ratio = sequence[i+1] / sequence[i]
            ratios.append(ratio)
    if all(d == diffs[0] for d in diffs):
        return "Arithmetic", sequence
    elif all(abs(r - ratios[0]) < 1e-9 for r in ratios):
        return "Geometric", sequence
    else:
        return "None", sequence
if __name__ == '__main__':
    sequence1 = [2, 4, 6, 8]
    print(f"Sequence: {sequence1}")
    print(find_pattern_sequence(sequence1))
    sequence2 = [3, 6, 12, 24]
    print(f"Sequence: {sequence2}")
    print(find_pattern_sequence(sequence2))
    sequence3 = [1, 2, 4, 8]
    print(f"Sequence: {sequence3}")
    print(find_pattern_sequence(sequence3))
    sequence4 = [1, 3, 5, 7]
    print(f"Sequence: {sequence4}")
    print(find_pattern_sequence(sequence4))
    sequence5 = [1, 2, 3, 5]
    print(f"Sequence: {sequence5}")
    print(find_pattern_sequence(sequence5))
    sequence6 = [10, 8, 6, 4]
    print(f"Sequence: {sequence6}")
    print(find_pattern_sequence(sequence6))
    sequence7 = [2, 3, 5, 8]
    print(f"Sequence: {sequence7}")
    print(find_pattern_sequence(sequence7))