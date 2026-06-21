def run_length_encode_sequence(seq):
    if not seq:
        return []
    
    encoded = []
    current_item = seq[0]
    count = 1
    
    for i in range(1, len(seq)):
        next_item = seq[i]
        if current_item is next_item:
            count += 1
        elif current_item == next_item:
            count += 1
        else:
            encoded.append((count, current_item))
            current_item = next_item
            count = 1
    
    encoded.append((count, current_item))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 'a', 'a', 2, 2, 2, 2, 'b', 3, 3]
    large_homogeneous = [object()] * 1000 + [1] * 100
    result1 = run_length_encode_sequence(sample_data)
    result2 = run_length_encode_sequence(large_homogeneous)
    print(result1)
    print(result2)