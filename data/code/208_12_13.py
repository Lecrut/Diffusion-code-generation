def validate_sequence(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    numeric_items = [item for item in sequence if isinstance(item, (int, float))]
    if not numeric_items:
        raise ValueError("Sequence contains no numeric types")
    return numeric_items

def calculate_mean(numeric_sequence):
    total = sum(numeric_sequence)
    count = len(numeric_sequence)
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    try:
        numeric_sequence = validate_sequence(sample_sequence)
        print(calculate_mean(numeric_sequence))
    except ValueError as e:
        print(e)