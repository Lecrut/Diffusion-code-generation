def run_length_encode(sequence):
    if not sequence:
        return []
    
    result = []
    current_item = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        item = sequence[i]
        if current_item is item or current_item == item:
            count += 1
        else:
            result.append((count, current_item))
            current_item = item
            count = 1
    
    result.append((count, current_item))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 'a', 'a', 'b', None, None, None, None]
    sample_data[0] = sample_data[1]
    sample_data[1] = sample_data[2]
    encoded = run_length_encode(sample_data)
    print(encoded)