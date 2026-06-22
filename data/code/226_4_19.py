import operator

def repeat_sequence(sequence):
    sequence.extend(operator.mul(sequence, 2))
    print(" ".join(map(str, sequence)))

if __name__ == '__main__':
    repeat_sequence(['a', 'b'])
    repeat_sequence([1, 2, 3])