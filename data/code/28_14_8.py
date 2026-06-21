def run_length_encode(sequence):
    if not sequence:
        return []
    
    encoded = []
    current_item = sequence[0]
    current_count = 1
    
    for i in range(1, len(sequence)):
        next_item = sequence[i]
        if current_item is next_item:
            current_count += 1
        else:
            encoded.append((current_item, current_count))
            current_item = next_item
            current_count = 1
    
    encoded.append((current_item, current_count))
    return encoded

if __name__ == '__main__':
    sample_data = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a']
    result = run_length_encode(sample_data)
    print(result)
    
    identical_a = object()
    identical_b = object()
    mixed_data = [identical_a, identical_a, identical_b, identical_a, identical_a, identical_a]
    result_mixed = run_length_encode(mixed_data)
    print(result_mixed)