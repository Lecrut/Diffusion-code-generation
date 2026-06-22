class BooleanChecker:
    def __init__(self, data):
        self.data = data
        self._cache = None

    def has_true(self):
        if self._cache is not None:
            return self._cache
        result = False
        for item in self.data:
            if item is True:
                result = True
                break
        self._cache = result
        return result

    def count_true(self):
        return sum(1 for x in self.data if x is True)

if __name__ == '__main__':
    checker = BooleanChecker([False, True, False])
    print(checker.has_true())
    print(checker.count_true())
    checker2 = BooleanChecker([False, False])
    print(checker2.has_true())