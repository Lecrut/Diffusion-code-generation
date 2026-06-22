def repeat_sequence(sequence, count):
    if not isinstance(sequence, list) or not all(isinstance(x, int) for x in sequence):
        raise ValueError("sequence must be a list of integers")
    if not isinstance(count, int) or count < 0:
        raise ValueError("count must be a non-negative integer")
    
    return sequence * count

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    sample_count = 3
    result = repeat_sequence(sample_sequence, sample_count)
    print(result)