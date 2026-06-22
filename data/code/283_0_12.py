class UniqueChecker:

    def __init__(self):
        self.seen = set()

    def add_element(self, item):
        if item in self.seen:
            return False
        self.seen.add(item)
        return True
if __name__ == '__main__':
    checker = UniqueChecker()
    print(checker.add_element(1))
    print(checker.add_element(2))
    print(checker.add_element(3))
    print(checker.add_element(1))