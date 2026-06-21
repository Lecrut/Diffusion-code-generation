def run_length_encode(sequence):
    if not sequence:
        return []

    encoded = []
    current_value = sequence[0]
    count = 1

    for value in sequence[1:]:
        if value == current_value:
            count += 1
        else:
            encoded.append([current_value, count])
            current_value = value
            count = 1

    encoded.append([current_value, count])
    return encoded

if __name__ == '__main__':
    sample_sequence = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5]
    result = run_length_encode(sample_sequence)
    print(result)

    empty_sequence = []
    empty_result = run_length_encode(empty_sequence)
    print(empty_result)

    single_element = [7]
    single_result = run_length_encode(single_element)
    print(single_result)

    mixed_sequence = [1, 2, 3, 4, 5]
    mixed_result = run_length_encode(mixed_sequence)
    print(mixed_result)

    negative_sequence = [-1, -1, -2, -2, -2, 0, 0]
    negative_result = run_length_encode(negative_sequence)
    print(negative_result)