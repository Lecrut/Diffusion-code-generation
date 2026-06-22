class EqualityChecker:
    def __init__(self, elements):
        self.elements = elements

    def all_equal(self):
        return len(set(self.elements)) == 1

if __name__ == '__main__':
    checker = EqualityChecker([5, 5, 5, 5])
    print(checker.all_equal())