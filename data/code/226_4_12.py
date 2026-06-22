import operator

def repeat_sequence(sequence, factor):
    if not isinstance(sequence, list) or not all(isinstance(item, str) for item in sequence):
        raise ValueError("Sequence must be a list of strings")
    if not isinstance(factor, int) or factor < 1:
        raise ValueError("Factor must be a positive integer")
    
    operator.setitem(sequence, slice(None), sequence * factor)

if __name__ == '__main__':
    sample_sequence = ['a', 'b', 'c']
    repeat_sequence(sample_sequence, 3)
    print(" ".join(sample_sequence))