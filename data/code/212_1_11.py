def find_min_max(sequence):
    if not sequence:
        return None, None
    
    min_val = max_val = sequence[0]
    
    for value in sequence[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
            
    return min_val, max_val

if __name__ == '__main__':
    sample_sequence = [3, 5, 1, 8, 2, 9, 4]
    print(find_min_max(sample_sequence))