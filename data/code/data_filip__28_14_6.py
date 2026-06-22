def run_length_encode(sequence):
    if not sequence:
        return []
    
    result = []
    current_value = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        next_value = sequence[i]
        if current_value is next_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = next_value
            count = 1
    
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
    encoded = run_length_encode(sample_sequence)
    print(encoded)
    
    sample_chars = ['a', 'a', 'b', 'b', 'b', 'c']
    encoded_chars = run_length_encode(sample_chars)
    print(encoded_chars)
    
    empty_sequence = []
    encoded_empty = run_length_encode(empty_sequence)
    print(encoded_empty)