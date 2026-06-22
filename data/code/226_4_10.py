import operator

def validate_input(value):
    if not isinstance(value, list) or len(value) != 1:
        raise ValueError('Input must be a list of exactly one character')

def repeat_sequence(sequence):
    validate_input(sequence)
    sequence.extend(operator.mul(sequence[0], 2))
    return sequence
if __name__ == '__main__':
    sample_list = ['a']
    result = repeat_sequence(sample_list)
    print(result)
    sample_list = ['b']
    result = repeat_sequence(sample_list)
    print(result)