def validate_sequence(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    return sequence

def sum_and_count_numbers(sequence):
    total = 0
    count = 0
    for item in sequence:
        if not isinstance(item, (int, float)):
            raise ValueError("Sequence contains non-numeric types")
        total += item
        count += 1
    return total, count

def calculate_mean(sequence):
    sequence = validate_sequence(sequence)
    total, count = sum_and_count_numbers(sequence)
    if count == 0:
        raise ValueError("Empty sequence")
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_sequence))