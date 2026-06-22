def detect_adjacent_mismatches(sequence):
    if not sequence or len(sequence) < 2:
        return []
    matches = list()
    prev_value = sequence[0]
    index = 0
    current_index = 1
    length = len(sequence)
    while current_index < length:
        curr_value = sequence[current_index]
        if prev_value != curr_value:
            matches.append((index, prev_value, curr_value))
        prev_value = curr_value
        index = current_index
        current_index += 1
    return matches

if __name__ == '__main__':
    test_data = [10, 10, 12, 12, 15, 10, 10, 20]
    result = detect_adjacent_mismatches(test_data)
    print(result)