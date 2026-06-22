def repeat_sequence(sequence, count):
    if not isinstance(sequence, list) or not all(isinstance(item, int) for item in sequence):
        raise ValueError("The first argument must be a list of integers.")
    if not isinstance(count, int) or count < 0:
        raise ValueError("The second argument must be a non-negative integer.")
    
    return sequence * count

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    sample_count = 3
    result = repeat_sequence(sample_sequence, sample_count)
    print(result)