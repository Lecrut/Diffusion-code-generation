def find_first_true(sequence):
    for item in sequence:
        if item:
            yield True
            return
if __name__ == '__main__':
    seq1 = [False, False, True, False]
    print(list(find_first_true(seq1)))
    seq2 = [False, False, False]
    print(list(find_first_true(seq2)))
    seq3 = [True, False, False]
    print(list(find_first_true(seq3)))
    seq4 = []
    print(list(find_first_true(seq4)))