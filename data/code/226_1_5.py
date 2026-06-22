from itertools import chain

def repeat_sequence(sequence, n):
    return list(chain.from_iterable([sequence] * n))

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    n = 3
    result = repeat_sequence(sample_sequence, n)
    print(result)