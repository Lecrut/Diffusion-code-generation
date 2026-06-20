class DuplicateChecker:

    def __init__(self):
        self.seen = set()

    def has_duplicates(self, lst):
        for item in lst:
            if item in self.seen:
                return True
            self.seen.add(item)
        return False
if __name__ == '__main__':
    checker = DuplicateChecker()
    print(checker.has_duplicates([1, 2, 3, 4]))
    print(checker.has_duplicates([1, 2, 3, 3]))
    print(checker.has_duplicates(['a', 'b', 'c', 'a']))