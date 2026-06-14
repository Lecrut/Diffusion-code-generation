def find_pattern_sequence(sequence):
    n = len(sequence)
    if n < 2:
        return "Neither", sequence
    is_arithmetic = True
    diff = sequence[1] - sequence[0]
    for i in range(2, n):
        if sequence[i] - sequence[i-1] != diff:
            is_arithmetic = False
            break
    if is_arithmetic:
        return "Arithmetic", sequence
    is_geometric = True
    if sequence[0] == 0 and any(x != 0 for x in sequence):
        pass
    else:
        for i in range(1, n):
            if sequence[i-1] == 0:
                if sequence[i] != 0:
                    is_geometric = False
                    break
            elif sequence[i] % sequence[i-1] != 0:
                is_geometric = False
                break
            elif sequence[i] / sequence[i-1] != sequence[i] / sequence[i-1]:
                 pass                                                                                                         
    if not is_geometric:
        return "Neither", sequence
    first_term = sequence[0]
    if first_term == 0:
        if all(x == 0 for x in sequence):
            return "Arithmetic", sequence                        
        else:
            return "Neither", sequence
    ratio = sequence[1] / sequence[0]
    for i in range(2, n):
        if abs(sequence[i] / sequence[i-1] - ratio) > 1e-9:
            is_geometric = False
            break
    if is_geometric:
        return "Geometric", sequence
    else:
        return "Neither", sequence
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
    sequence7 = [2, 3, 5, 8]
    print(f"Sequence: {sequence7}, Pattern: {find_pattern_sequence(sequence7)}")
    sequence8 = [1, 1, 1, 1]
    print(f"Sequence: {sequence8}, Pattern: {find_pattern_sequence(sequence8)}")
    sequence9 = [10, 5, 2.5, 1.25]
    print(f"Sequence: {sequence9}, Pattern: {find_pattern_sequence(sequence9)}")