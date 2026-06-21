def validate_sequence(sequence):
    if not hasattr(sequence, '__iter__'):
        raise ValueError("Input is not iterable")
    return sequence

def count_valid_numbers(sequence):
    count = 0
    for item in sequence:
        if isinstance(item, (int, float)):
            count += 1
    if count == 0:
        raise ValueError("Empty sequence containing only non-numeric types")
    return count

def sum_valid_numbers(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (int, float)):
            total += item
    return total

def calculate_mean(sequence):
    validated_sequence = validate_sequence(sequence)
    count = count_valid_numbers(validated_sequence)
    total = sum_valid_numbers(validated_sequence)
    return float(total / count)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_sequence))