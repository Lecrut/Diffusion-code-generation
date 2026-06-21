def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    total = sum(item for item in sequence if isinstance(item, (int, float)))
    count = len([item for item in sequence if isinstance(item, (int, float))])
    if count == 0:
        raise ValueError("Empty sequence")
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [15, 25, 35, 45]
    print(calculate_mean(sample_sequence))