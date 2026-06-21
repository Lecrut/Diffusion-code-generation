def run_length_encode(sequence):
    if not sequence:
        return []
    
    result = []
    current_item = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        item = sequence[i]
        if item == current_item:
            count += 1
        else:
            result.append((current_item, count))
            current_item = item
            count = 1
    
    result.append((current_item, count))
    
    return result

if __name__ == '__main__':
    data = [1, 1, 2, 3, 3, 3, 4]
    encoded = run_length_encode(data)
    print(encoded)