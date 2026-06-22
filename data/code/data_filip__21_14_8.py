def run_length_encode(sequence):
    if not sequence:
        return []
    result = []
    current_value = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_value:
            count += 1
        else:
            result.append((count, current_value))
            current_value = sequence[i]
            count = 1
    result.append((count, current_value))
    return result

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5, 5, 5]
    encoded_result = run_length_encode(sample_sequence)
    print(encoded_result)