def extend_array(sequence, num_repeats):
    array_length = len(sequence)
    sequence *= num_repeats
    return sequence

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    repeated_sequence = extend_array(sample_sequence, 5)
    print(repeated_sequence)