class TruthChecker:
    FALSE_STATES = {False, None, 0, 0.0, '', [], {}, set()}

    @staticmethod
    def is_false(val):
        return val in TruthChecker.FALSE_STATES

    @staticmethod
    def both_false(x, y):
        return TruthChecker.is_false(x) and TruthChecker.is_false(y)

if __name__ == '__main__':
    x = 0
    y = None
    result = TruthChecker.both_false(x, y)
    print(result)