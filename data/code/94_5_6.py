def first_true(sequence):
    return any(sequence)

if __name__ == '__main__':
    sample_sequence = [False, False, True, False]
    print(first_true(sample_sequence))