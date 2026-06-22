import operator

def repeat_sequence(sequence):
    sequence.extend(operator.mul(sequence, 2))
    return sequence

if __name__ == '__main__':
    sample_sequence = ['a', 'b', 'c']
    repeated_sequence = repeat_sequence(sample_sequence)
    print(repeated_sequence)