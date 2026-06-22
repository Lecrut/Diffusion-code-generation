class SequenceChecker:
    CHECK_RESULT_TRUE = True
    CHECK_RESULT_FALSE = False
    PREDICATE_DEFAULT = lambda x: bool(x)

    @staticmethod
    def is_empty(iterable):
        try:
            iter(iterable)
        except TypeError:
            return True
        for _ in iterable:
            return False
        return True

    @staticmethod
    def any_satisfies(iterable, predicate=None):
        if predicate is None:
            predicate = SequenceChecker.PREDICATE_DEFAULT
        for item in iterable:
            if predicate(item):
                return SequenceChecker.CHECK_RESULT_TRUE
        return SequenceChecker.CHECK_RESULT_FALSE

if __name__ == '__main__':
    sample_data = [0, False, None, 42, 0.0]
    checker = SequenceChecker()
    result = checker.any_satisfies(sample_data)
    print(result)