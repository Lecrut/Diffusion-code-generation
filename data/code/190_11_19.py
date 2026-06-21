class ListChecker:

    def __init__(self, items):
        self.items = items

    def contains(self, item):
        return item in self.items
if __name__ == '__main__':
    checker = ListChecker([10, 25, 33, 42, 56, 78, 91])
    print(checker.contains(42))
    print(checker.contains(100))