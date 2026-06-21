def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    
    total = 0
    count = 0
    
    for item in sequence:
        if not isinstance(item, (int, float)):
            raise ValueError("Sequence contains non-numeric types")
        
        total += item
        count += 1
    
    if count == 0:
        raise ValueError("Empty sequence")
    
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(calculate_mean(sample_sequence))