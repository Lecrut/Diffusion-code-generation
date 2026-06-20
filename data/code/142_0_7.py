class BooleanEquivalenceChecker:
    def check_equivalence(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    checker = BooleanEquivalenceChecker()
    print(checker.check_equivalence(True, False))
    print(checker.check_equivalence(False, False))
    print(checker.check_equivalence(True, True))