class UniqueChecker:
    def __init__(self):
        self.seen = set()

    def add(self, item):
        if item in self.seen:
            return False
        self.seen.add(item)
        return True

if __name__ == '__main__':
    checker = UniqueChecker()
    sample_list = [1, 2, 3, 4, 5]
    for item in sample_list:
        print(checker.add(item))

    sample_list_with_duplicates = [1, 2, 3, 3, 5]
    checker.reset()
    for item in sample_list_with_duplicates:
        print(checker.add(item))