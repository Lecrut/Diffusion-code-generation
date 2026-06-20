class BooleanEquivalenceChecker:
    EQUIVALENCE_MESSAGE = 'Equal'
    DIFFERENT_VALUE_MESSAGE = 'One is True, the other is False'

    @staticmethod
    def check_equivalence(a: bool, b: bool) -> str:
        if a == b:
            return BooleanEquivalenceChecker.EQUIVALENCE_MESSAGE
        elif (a and not b) or (not a and b):
            return BooleanEquivalenceChecker.DIFFERENT_VALUE_MESSAGE

if __name__ == '__main__':
    checker = BooleanEquivalenceChecker()
    print(checker.check_equivalence(True, True))
    print(checker.check_equivalence(True, False))
    print(checker.check_equivalence(False, True))
    print(checker.check_equivalence(False, False))