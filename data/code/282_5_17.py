MAX_SEQUENCE_LENGTH = 1000

def sum_sequence(sequence):
    return sum(x for x in sequence if isinstance(x, int) and -MAX_SEQUENCE_LENGTH <= x <= MAX_SEQUENCE_LENGTH)

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5]
    result = sum_sequence(sample_sequence)
    print(result)