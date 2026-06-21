def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    numeric_values = [item for item in sequence if isinstance(item, (int, float))]
    if not numeric_values:
        raise ValueError("Empty sequence or no numeric values")
    return float(sum(numeric_values) / len(numeric_values))

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_sequence))