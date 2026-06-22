def run_length_encode(sequence):
    if not sequence:
        return []
    
    encoded = []
    current_item = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        next_item = sequence[i]
        if next_item is current_item or next_item == current_item:
            count += 1
        else:
            encoded.append((current_item, count))
            current_item = next_item
            count = 1
    
    encoded.append((current_item, count))
    return encoded

if __name__ == '__main__':
    sample_data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'a']
    result = run_length_encode(sample_data)
    print(result)