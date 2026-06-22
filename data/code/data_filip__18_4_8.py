def run_length_encode(sequence):
    if not sequence:
        return []
    result = []
    current_value = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        value = sequence[i]
        if value == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = value
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_sequence = [1, 1, 2, 3, 3, 3, 4]
    encoded_sequence = run_length_encode(sample_sequence)
    print(encoded_sequence)