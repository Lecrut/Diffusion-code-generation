class BooleanSequenceChecker:
    def __init__(self, sequence):
        self.sequence = sequence

    def find_first_true(self):
        for item in self.sequence:
            if item:
                yield True
                return
        yield False

if __name__ == '__main__':
    checker1 = BooleanSequenceChecker([False, False, True, False])
    result1 = next(checker1.find_first_true())
    print(f"First True in {checker1.sequence}: {result1}")

    checker2 = BooleanSequenceChecker([False, False, False])
    result2 = next(checker2.find_first_true())
    print(f"First True in {checker2.sequence}: {result2}")

    checker3 = BooleanSequenceChecker([True, False, True])
    result3 = next(checker3.find_first_true())
    print(f"First True in {checker3.sequence}: {result3}")