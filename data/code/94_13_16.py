class TruthyChecker:
    def __init__(self, sequence):
        self._sequence = sequence

    def check(self, predicate=None):
        if predicate is None:
            for item in self._sequence:
                if item:
                    return True
            return False
        for item in self._sequence:
            if predicate(item):
                return True
        return False

    def get_first_truthy(self, predicate=None):
        if predicate is None:
            for item in self._sequence:
                if item:
                    return item
            return None
        for item in self._sequence:
            if predicate(item):
                return item
        return None

if __name__ == '__main__':
    checker = TruthyChecker([0, 0, 0, 42, 0])
    result1 = checker.check(lambda x: x > 40)
    print(result1)
    result2 = checker.get_first_truthy(lambda x: x > 40)
    print(result2)
    result3 = checker.check()
    print(result3)
    result4 = checker.get_first_truthy()
    print(result4)