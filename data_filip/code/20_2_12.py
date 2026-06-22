def rle_compress(binary_sequence):
    if not binary_sequence:
        return []
    
    compressed = []
    current_value = binary_sequence[0]
    count = 1
    
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == current_value:
            count += 1
        else:
            compressed.append((current_value, count))
            current_value = binary_sequence[i]
            count = 1
    
    compressed.append((current_value, count))
    return compressed

if __name__ == '__main__':
    sample_data = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]
    result = rle_compress(sample_data)
    print(result)