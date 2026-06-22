def extend_static_array(sequence, num_repeats):
    if not sequence or not isinstance(sequence, list) or not all(isinstance(item, int) for item in sequence):
        raise ValueError("Sequence must be a non-empty list of integers")
    if not isinstance(num_repeats, int) or num_repeats <= 0:
        raise ValueError("Number of repeats must be a positive integer")

    sequence_length = len(sequence)
    full_sequence = (sequence * num_repeats)[:sequence_length]
    
    return full_sequence

if __name__ == '__main__':
    initial_sequence = [1, 2, 3]
    num_repeats = 5
    result = extend_static_array(initial_sequence, num_repeats)
    print(result)