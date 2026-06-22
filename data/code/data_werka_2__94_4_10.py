class BooleanListChecker:
    def __init__(self, flags):
        self.flags = flags

    def has_true_value(self):
        if not self.flags:
            return False
        return any(self.flags)

if __name__ == '__main__':
    checker1 = BooleanListChecker([False, False, False])
    checker2 = BooleanListChecker([False, True, False])
    checker3 = BooleanListChecker([])
    checker4 = BooleanListChecker([True])
    checker5 = BooleanListChecker([False, False, True])

    print(checker1.has_true_value())
    print(checker2.has_true_value())
    print(checker3.has_true_value())
    print(checker4.has_true_value())
    print(checker5.has_true_value())