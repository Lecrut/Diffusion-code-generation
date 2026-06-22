def run_length_encode(sequence):
    if not sequence:
        return []
    
    result = []
    current_item = sequence[0]
    count = 1
    
    for item in sequence[1:]:
        if item == current_item:
            count += 1
        else:
            result.append((current_item, count))
            current_item = item
            count = 1
    
    result.append((current_item, count))
    return result

if __name__ == '__main__':
    sample_sequence = [1, 1, 2, 3, 3, 3, 4]
    encoded_result = run_length_encode(sample_sequence)
    print(encoded_result)