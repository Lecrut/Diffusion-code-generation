def run_length_encode(sequence):
    if not sequence:
        return []

    encoded = []
    current_value = sequence[0]
    current_count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == current_value:
            current_count += 1
        else:
            encoded.append([current_value, current_count])
            current_value = sequence[i]
            current_count = 1

    encoded.append([current_value, current_count])
    return encoded

if __name__ == '__main__':
    sample_input = [1, 1, 1, 2, 3, 3, 2, 2, 4]
    result = run_length_encode(sample_input)
    print(result)