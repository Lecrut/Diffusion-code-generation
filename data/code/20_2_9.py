def run_length_encode(binary_sequence):
    if not binary_sequence:
        return []
    
    compressed = []
    current_val = binary_sequence[0]
    count = 1
    
    for i in range(1, len(binary_sequence)):
        if binary_sequence[i] == current_val:
            count += 1
        else:
            compressed.append((current_val, count))
            current_val = binary_sequence[i]
            count = 1
    
    compressed.append((current_val, count))
    return compressed

if __name__ == '__main__':
    sample_sequence = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1]
    result = run_length_encode(sample_sequence)
    print(result)