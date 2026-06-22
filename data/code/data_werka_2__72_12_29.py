def get_adjacent_mismatches(sequence):
    mismatches = []
    count = len(sequence)
    if count < 2:
        return mismatches
    index = 0
    while index < count - 1:
        current_val = sequence[index]
        next_val = sequence[index + 1]
        if current_val != next_val:
            mismatches.append((index, current_val, next_val))
        index += 1
    return mismatches

if __name__ == '__main__':
    test_sequence = [10, 10, 15, 15, 20, 25, 25, 30]
    result = get_adjacent_mismatches(test_sequence)
    print(result)