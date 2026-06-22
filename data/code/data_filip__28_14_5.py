def run_length_encode(sequence):
    if not sequence:
        return []
    
    encoded = []
    current_item = sequence[0]
    count = 1
    
    for item in sequence[1:]:
        if item is current_item:
            count += 1
        elif item == current_item and not (id(item) != id(current_item)):
            count += 1
        else:
            encoded.append((current_item, count))
            current_item = item
            count = 1
    
    encoded.append((current_item, count))
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    result = run_length_encode(sample_data)
    print(result)