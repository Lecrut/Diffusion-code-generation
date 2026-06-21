def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input must be iterable")
    
    total = 0
    count = 0
    
    for item in sequence:
        if isinstance(item, (int, float)):
            total += item
            count += 1
        else:
            raise ValueError("All elements in the sequence must be numeric")
    
    if count == 0:
        raise ValueError("Sequence must contain at least one number")
    
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(calculate_mean(sample_sequence))