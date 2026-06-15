def find_pattern_sequence(sequence):
    n = len(sequence)
    if n <= 1:
        return "None", sequence
    is_arithmetic = True
    diff = sequence[1] - sequence[0]
    for i in range(2, n):
        if sequence[i] - sequence[i-1] != diff:
            is_arithmetic = False
            break
    if is_arithmetic:
        return "Arithmetic", sequence
    is_geometric = True
    if sequence[0] != 0:
        ratio = sequence[1] / sequence[0]
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
    if all(x == sequence[0] for x in sequence):
        return "Arithmetic", sequence
    return "None", sequence
if __name__ == '__main__':
    sequence1 = [2, 4, 6, 8]
    print(f"Sequence: {sequence1}, Pattern: {find_pattern_sequence(sequence1)}")
    sequence2 = [1, 2, 3, 4]
    print(f"Sequence: {sequence2}, Pattern: {find_pattern_sequence(sequence2)}")
    sequence3 = [2, 4, 8, 16]
    print(f"Sequence: {sequence3}, Pattern: {find_pattern_sequence(sequence3)}")
    sequence4 = [1, 3, 5, 7]
    print(f"Sequence: {sequence4}, Pattern: {find_pattern_sequence(sequence4)}")
    sequence5 = [1, 2, 4, 8]
    print(f"Sequence: {sequence5}, Pattern: {find_pattern_sequence(sequence5)}")
    sequence6 = [3, 6, 9, 12]
    print(f"Sequence: {sequence6}, Pattern: {find_pattern_sequence(sequence6)}")
    sequence7 = [1, 2, 3, 5]
    print(f"Sequence: {sequence7}, Pattern: {find_pattern_sequence(sequence7)}")
    sequence8 = [5, 5, 5, 5]
    print(f"Sequence: {sequence8}, Pattern: {find_pattern_sequence(sequence8)}")
    sequence9 = [10, 5, 0, -5]
    print(f"Sequence: {sequence9}, Pattern: {find_pattern_sequence(sequence9)}")