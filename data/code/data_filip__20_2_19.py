def compress_binary_sequence(sequence):
    if not sequence:
        return []
    result = []
    current_value = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = sequence[i]
            count = 1
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1]
    compressed_data = compress_binary_sequence(sample_sequence)
    print(compressed_data)