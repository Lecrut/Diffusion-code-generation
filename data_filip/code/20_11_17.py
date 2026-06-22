def encode_numeric_sequence(sequence):
    if not sequence:
        return []
    encoded_list = []
    current_digit = sequence[0]
    occurrence_count = 1
    iterator = iter(sequence)
    next(iterator)
    for char in iterator:
        if char == current_digit:
            occurrence_count += 1
        else:
            encoded_list.append([int(current_digit), occurrence_count])
            current_digit = char
            occurrence_count = 1
    encoded_list.append([int(current_digit), occurrence_count])
    return encoded_list

if __name__ == '__main__':
    test_input = "99900001122222"
    final_output = encode_numeric_sequence(test_input)
    print(final_output)