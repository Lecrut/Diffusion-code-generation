def compress_rle(binary_sequence):
    if not binary_sequence:
        return []
    
    result = []
    current_value = binary_sequence[0]
    count = 1
    
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = binary_sequence[i]
            count = 1
    
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    compressed = compress_rle(sample_sequence)
    print(compressed)