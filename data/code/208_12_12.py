def calculate_mean(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    numeric_values = [item for item in sequence if isinstance(item, (int, float))]
    if len(numeric_values) == 0:
        raise ValueError("Empty sequence or no numeric values")
    return float(sum(numeric_values)) / len(numeric_values)

if __name__ == '__main__':
    sample_sequence = [12, 24, 36, 48]
    print(calculate_mean(sample_sequence))