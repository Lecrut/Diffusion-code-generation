def get_adjacent_mismatches(sequence):
    if not sequence or len(sequence) < 2:
        return []
    mismatches = []
    prev = sequence[0]
    for idx in range(1, len(sequence)):
        curr = sequence[idx]
        if prev != curr:
            mismatches.append((idx - 1, prev, curr))
        prev = curr
    return mismatches

if __name__ == '__main__':
    test_values = [10, 10, 20, 30, 30, 40, 50, 50]
    result = get_adjacent_mismatches(test_values)
    print(result)