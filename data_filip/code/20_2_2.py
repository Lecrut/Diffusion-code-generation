def rle_compress(binary_sequence):
    if not binary_sequence:
        return []
    compressed = []
    current_bit = binary_sequence[0]
    count = 1
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == current_bit:
            count += 1
        else:
            compressed.append((current_bit, count))
            current_bit = binary_sequence[i]
            count = 1
    compressed.append((current_bit, count))
    return compressed

if __name__ == '__main__':
    sample_sequence = [0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    result = rle_compress(sample_sequence)
    print(result)