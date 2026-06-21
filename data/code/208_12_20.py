def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    
    total = 0
    count = 0
    for item in sequence:
        if isinstance(item, (int, float)):
            total += item
            count += 1
        else:
            raise ValueError("Sequence contains non-numeric types")
    
    if count == 0:
        raise ValueError("Empty sequence")
    
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    print(calculate_mean(sample_sequence))