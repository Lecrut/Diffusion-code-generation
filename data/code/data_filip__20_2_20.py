def run_length_encode(sequence):
    if not sequence:
        return []
    encoded = []
    current_value = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_value:
            count += 1
        else:
            encoded.append((count, current_value))
            current_value = sequence[i]
            count = 1
    encoded.append((count, current_value))
    return encoded

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    result = run_length_encode(sample_sequence)
    print(result)