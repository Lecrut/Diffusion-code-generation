class BooleanChecker:
    def __init__(self, flags):
        self.flags = flags

    def has_true(self):
        if not self.flags:
            return False
        return any(self.flags)

if __name__ == '__main__':
    checker1 = BooleanChecker([False, False, False])
    checker2 = BooleanChecker([False, True, False])
    checker3 = BooleanChecker([])
    checker4 = BooleanChecker([True])
    checker5 = BooleanChecker([False, False, False, False])
    
    print(checker1.has_true())
    print(checker2.has_true())
    print(checker3.has_true())
    print(checker4.has_true())
    print(checker5.has_true())