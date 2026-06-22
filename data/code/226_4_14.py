from operator import setitem

def validate_sequence(sequence):
    if not isinstance(sequence, list) or not sequence:
        raise ValueError('Sequence must be a non-empty list')
    return sequence

def repeat_sequence(seq):
    seq = validate_sequence(seq)
    original_length = len(seq)
    for _ in range(2):
        for i in range(original_length):
            setitem(seq, len(seq), seq[i])
    return seq
if __name__ == '__main__':
    sample_seq = ['a', 'b', 'c']
    result = repeat_sequence(sample_seq)
    print(result)