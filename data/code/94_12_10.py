class TruthyChecker:
    def __init__(self, data):
        self.data = data

    def contains_truthy(self):
        return any(self.data)

if __name__ == '__main__':
    checker1 = TruthyChecker([0, 0, 0])
    print(checker1.contains_truthy())
    checker2 = TruthyChecker([0, 1, 0])
    print(checker2.contains_truthy())
    checker3 = TruthyChecker([])
    print(checker3.contains_truthy())
    checker4 = TruthyChecker([None, False, 0])
    print(checker4.contains_truthy())
    checker5 = TruthyChecker([None, False, 1])
    print(checker5.contains_truthy())