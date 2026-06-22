def compress_rle(binary_sequence):
    if not binary_sequence:
        return []
    if isinstance(binary_sequence, str):
        binary_sequence = [int(b) for b in binary_sequence]
    compressed = []
    if not binary_sequence:
        return compressed
    current_value = binary_sequence[0]
    run_length = 1
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == current_value:
            run_length += 1
        else:
            compressed.append((current_value, run_length))
            current_value = binary_sequence[i]
            run_length = 1
    compressed.append((current_value, run_length))
    return compressed
if __name__ == '__main__':
    sample_binary = '111100111110000111'
    result = compress_rle(sample_binary)
    print(result)