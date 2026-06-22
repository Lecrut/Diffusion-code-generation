from itertools import chain

def repeat_sequence(sequence, count):
    repeated_sequences = [sequence] * count
    result = list(chain.from_iterable(repeated_sequences))
    return result

if __name__ == '__main__':
    sample_seq = ['a', 'b', 'c']
    repeat_count = 2
    output = repeat_sequence(sample_seq, repeat_count)
    print(output)