def find_first_true(sequence):
    return any((item for item in sequence))
if __name__ == '__main__':
    seq1 = [False, False, True, False]
    print(find_first_true(seq1))
    seq2 = [False, False, False]
    print(find_first_true(seq2))
    seq3 = [True, False, True]
    print(find_first_true(seq3))