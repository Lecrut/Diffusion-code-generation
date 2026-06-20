class BooleanEquivalenceChecker:
    @staticmethod
    def are_booleans_equivalent(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = BooleanEquivalenceChecker.are_booleans_equivalent(sample_a, sample_b)
    print(result)