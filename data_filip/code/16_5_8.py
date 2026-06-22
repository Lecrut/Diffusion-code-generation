def run_length_encoding(sequence):
    if not sequence:
        return []
    encoded = []
    current_value = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_value:
            count += 1
        else:
            encoded.append([current_value, count])
            current_value = sequence[i]
            count = 1
    encoded.append([current_value, count])
    return encoded

if __name__ == '__main__':
    sample_input = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
    result = run_length_encoding(sample_input)
    print(result)