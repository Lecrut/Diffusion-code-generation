class TruthChecker:
    FALSE_VALUES = {False, 0, 0.0, '', [], {}, None}

    @staticmethod
    def is_false(value):
        return value in TruthChecker.FALSE_VALUES

    @staticmethod
    def both_false(x, y):
        return TruthChecker.is_false(x) and TruthChecker.is_false(y)

if __name__ == '__main__':
    x = None
    y = 0
    result = TruthChecker.both_false(x, y)
    print(result)