def compress_binary_rle(binary_sequence):
    if not binary_sequence:
        return []
    
    compressed = []
    current_char = binary_sequence[0]
    count = 1
    
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == current_char:
            count += 1
        else:
            compressed.append((current_char, count))
            current_char = binary_sequence[i]
            count = 1
    
    compressed.append((current_char, count))
    return compressed

if __name__ == '__main__':
    sample_sequence = "00001110011111100000000011111"
    result = compress_binary_rle(sample_sequence)
    print(result)