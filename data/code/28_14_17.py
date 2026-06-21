def run_length_encode(sequence):
    if not sequence:
        return []
    
    result = []
    current_item = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        next_item = sequence[i]
        if next_item is current_item:
            count += 1
        elif next_item == current_item:
            count += 1
        else:
            result.append((count, current_item))
            current_item = next_item
            count = 1
    
    result.append((count, current_item))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 2, 3, 3, 'a', 'a', 'a', 'a', None, None, 0, 0, 0]
    sample_data = [None] * 10 + [0] * 5 + [None] * 3
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)