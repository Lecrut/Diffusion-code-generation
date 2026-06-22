class BooleanSequenceChecker:
    def __init__(self, sequence):
        self._sequence = sequence

    def has_true(self):
        for val in self._sequence:
            if val:
                return True
        return False

    def find_first_true_generator(self):
        for val in self._sequence:
            if val:
                yield True
                return
        yield False

if __name__ == '__main__':
    seq1 = [False, False, True, False]
    seq2 = [False, False, False]
    seq3 = [True, False, True]

    checker1 = BooleanSequenceChecker(seq1)
    print(checker1.has_true())

    checker2 = BooleanSequenceChecker(seq2)
    print(checker2.has_true())

    gen1 = BooleanSequenceChecker(seq3).find_first_true_generator()
    print(next(gen1))