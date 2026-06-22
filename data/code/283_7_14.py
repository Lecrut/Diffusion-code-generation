class ElementChecker:
    def __init__(self, elements):
        self.elements = elements

    def are_all_equal(self):
        return len(set(self.elements)) == 1

if __name__ == '__main__':
    checker = ElementChecker([42, 42, 42])
    print(checker.are_all_equal())