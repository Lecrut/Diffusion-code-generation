def find_pattern_sequence(sequence):
    n = len(sequence)
    if n <= 1:
        return "Unknown", sequence
    if n == 2:
        if sequence[0] != 0:
            if sequence[1] - sequence[0] != 0:
                return "Arithmetic", sequence
        return "Arithmetic", sequence
    diff = sequence[1] - sequence[0]
    is_arithmetic = True
    for i in range(2, n):
        if sequence[i] - sequence[i-1] != diff:
            is_arithmetic = False
            break
    if is_arithmetic:
        return "Arithmetic", sequence
    if sequence[0] == 0:
        all_zero = all(x == 0 for x in sequence)
        if all_zero:
            return "Arithmetic", sequence
        pass
    if sequence[0] != 0:
        ratio = sequence[1] / sequence[0]
        is_geometric = True
        for i in range(2, n):
            if sequence[i-1] == 0:
                is_geometric = False
                break
            current_ratio = sequence[i] / sequence[i-1]
            if abs(current_ratio - ratio) > 1e-9:
                is_geometric = False
                break
        if is_geometric:
            return "Geometric", sequence
    return "Unknown", sequence
if __name__ == '__main__':
    sequence1 = [2, 4, 6, 8]
    result1 = find_pattern_sequence(sequence1)
    print(f"Sequence: {sequence1}, Pattern: {result1[0]}, Sequence: {result1[1]}")
    sequence2 = [3, 6, 12, 24]
    result2 = find_pattern_sequence(sequence2)
    print(f"Sequence: {sequence2}, Pattern: {result2[0]}, Sequence: {result2[1]}")
    sequence3 = [1, 2, 4, 8]
    result3 = find_pattern_sequence(sequence3)
    print(f"Sequence: {sequence3}, Pattern: {result3[0]}, Sequence: {result3[1]}")
    sequence4 = [1, 3, 5, 7]
    result4 = find_pattern_sequence(sequence4)
    print(f"Sequence: {sequence4}, Pattern: {result4[0]}, Sequence: {result4[1]}")
    sequence5 = [1, 2, 3, 5]
    result5 = find_pattern_sequence(sequence5)
    print(f"Sequence: {sequence5}, Pattern: {result5[0]}, Sequence: {result5[1]}")
    sequence6 = [10, 5, 0, -5]
    result6 = find_pattern_sequence(sequence6)
    print(f"Sequence: {sequence6}, Pattern: {result6[0]}, Sequence: {result6[1]}")
    sequence7 = [5, 5, 5, 5]
    result7 = find_pattern_sequence(sequence7)
    print(f"Sequence: {sequence7}, Pattern: {result7[0]}, Sequence: {result7[1]}")