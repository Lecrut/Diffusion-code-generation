def run_length_encode(sequence):
    if not sequence:
        return []
    
    result = []
    current_item = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        next_item = sequence[i]
        if current_item is next_item:
            count += 1
        else:
            result.append((count, current_item))
            current_item = next_item
            count = 1
    
    result.append((count, current_item))
    return result

if __name__ == '__main__':
    a = object()
    b = object()
    c = object()
    sample_data = [a, a, a, b, b, c, c, c, c, a]
    encoded = run_length_encode(sample_data)
    print(encoded)