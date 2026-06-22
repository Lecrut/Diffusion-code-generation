def compress_binary_sequence(sequence):
    if not sequence:
        return []
    compressed = []
    current_char = sequence[0]
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = sequence[i]
            count = 1
    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]
    result = compress_binary_sequence(sample_sequence)
    print(result)