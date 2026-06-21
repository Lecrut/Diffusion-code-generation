NUMERIC_TYPES = (int, float)

def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    
    total = sum(item for item in sequence if isinstance(item, NUMERIC_TYPES))
    count = len([item for item in sequence if isinstance(item, NUMERIC_TYPES)])
    
    if count == 0:
        raise ValueError("Empty sequence")
    
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_sequence))