class BooleanChecker:
    BOTH_FALSE = (False, False)

    @staticmethod
    def _is_false_pair(val1, val2):
        return val1 is False and val2 is False

    @classmethod
    def both_false_generator(cls, a, b):
        if cls._is_false_pair(a, b):
            yield True
        else:
            yield False

if __name__ == '__main__':
    checker = BooleanChecker()
    result = list(checker.both_false_generator(False, False))
    print(result)
    result2 = list(checker.both_false_generator(True, False))
    print(result2)