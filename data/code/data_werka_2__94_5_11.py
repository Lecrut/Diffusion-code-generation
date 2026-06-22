class BooleanSequenceChecker:
    def __init__(self, sequence):
        self._sequence = sequence

    def has_first_true(self):
        for item in self._sequence:
            if item:
                return True
        return False

    def find_first_true_index(self):
        for index, item in enumerate(self._sequence):
            if item:
                return index
        return -1

if __name__ == '__main__':
    seq1 = [False, False, True, False]
    checker1 = BooleanSequenceChecker(seq1)
    print(checker1.has_first_true())
    print(checker1.find_first_true_index())

    seq2 = [False, False, False]
    checker2 = BooleanSequenceChecker(seq2)
    print(checker2.has_first_true())
    print(checker2.find_first_true_index())

    seq3 = [True, False, True]
    checker3 = BooleanSequenceChecker(seq3)
    print(checker3.has_first_true())
    print(checker3.find_first_true_index())