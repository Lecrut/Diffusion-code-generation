import operator

def extend_list(sequence, factor):
    sequence.extend(operator.mul(sequence[0], factor))

if __name__ == '__main__':
    sample = ['a', 'b', 'c']
    extend_list(sample, 3)
    print(" ".join(sample))