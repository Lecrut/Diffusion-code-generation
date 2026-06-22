import operator

def extend_list(sequence, factor):
    operator.setitem(sequence, slice(None), sequence + sequence[:factor])

if __name__ == '__main__':
    sample = ['a', 'b', 'c']
    extend_list(sample, 3)
    print(" ".join(sample))
    
    sample = ['x', 'y']
    extend_list(sample, 2)
    print(" ".join(sample))