def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    
    numeric_items = [item for item in sequence if isinstance(item, (int, float))]
    if not numeric_items:
        raise ValueError("No numeric types found in the sequence")
    
    total = sum(numeric_items)
    count = len(numeric_items)
    
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [3.5, 4.2, 6.8]
    print(calculate_mean(sample_sequence))