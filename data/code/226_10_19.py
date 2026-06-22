SEQUENCE_MULTIPLIER = 3

def repeat_sequence(sequence, count):
    return sequence * count
if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    sample_count = SEQUENCE_MULTIPLIER
    result = repeat_sequence(sample_sequence, sample_count)
    print(result)