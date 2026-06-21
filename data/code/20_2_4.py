def run_length_encode(sequence):
    if not sequence:
        return []
    
    encoded = []
    count = 1
    current_val = sequence[0]
    
    for i in range(1, len(sequence)):
        val = sequence[i]
        if val == current_val:
            count += 1
        else:
            encoded.append((current_val, count))
            current_val = val
            count = 1
    encoded.append((current_val, count))
    return encoded

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 2, 3, 3, 2, 2, 2, 2]
    result = run_length_encode(sample_sequence)
    print(result)