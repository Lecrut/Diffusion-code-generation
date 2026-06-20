class BooleanEquivalenceChecker:
    @staticmethod
    def check_equivalence(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    result = BooleanEquivalenceChecker.check_equivalence(True, False)
    print(result)