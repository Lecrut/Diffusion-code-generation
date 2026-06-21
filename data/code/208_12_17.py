def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    numeric_items = [item for item in sequence if isinstance(item, (int, float))]
    if not numeric_items:
        raise ValueError("No numeric values found in the input")
    total = sum(numeric_items)
    count = len(numeric_items)
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_sequence))