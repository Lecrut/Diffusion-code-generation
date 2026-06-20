class TruthChecker:
    @staticmethod
    def at_least_one_true(iterable):
        return any(iterable)

if __name__ == '__main__':
    checker = TruthChecker()
    print(checker.at_least_one_true([True, False, True, False]))
    print(checker.at_least_one_true([False, False, False]))
    print(checker.at_least_one_true(['', '', 'hello']))
    print(checker.at_least_one_true([]))