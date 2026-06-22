import operator

def repeat_sequence(sequence, factor):
    sequence.extend(operator.mul(sequence, factor))
    return sequence

if __name__ == '__main__':
    sample = ['a', 'b', 'c']
    result = repeat_sequence(sample, 3)
    print(result)