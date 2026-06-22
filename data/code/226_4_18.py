import operator

def validate_input(sequence, factor):
    if not isinstance(sequence, list) or not all(isinstance(item, str) for item in sequence):
        raise ValueError("Sequence must be a list of strings")
    if not isinstance(factor, int) or factor <= 0:
        raise ValueError("Factor must be a positive integer")

def repeat_sequence(sequence, factor):
    validate_input(sequence, factor)
    sequence.extend(operator.mul(sequence, factor))
    return sequence

if __name__ == '__main__':
    print(repeat_sequence(['a', 'b'], 3))
    print(repeat_sequence(['x'], 2))
    print(repeat_sequence([], 1))