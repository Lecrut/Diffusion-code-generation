class ContradictionChecker:
    def check_contradictions(self, statements):
        n = len(statements)
        for i in range(n):
            for j in range(i + 1, n):
                s1 = statements[i]
                s2 = statements[j]
                if self._are_contradictory(s1, s2):
                    return True
        return False
    def _are_contradictory(self, s1, s2):
        s1_parts = [p.strip() for p in s1.split(' ')]
        s2_parts = [p.strip() for p in s2.split(' ')]
        if not s1_parts or not s2_parts:
            return False
        if 'not' in s1 and 'not' in s2:
            pass
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    sample_statements_1 = [
        "P",
        "Q",
        "R",
        "P and Q"
    ]
    sample_statements_2 = [
        "P",
        "not P",
        "Q"
    ]
    sample_statements_3 = [
        "A",
        "not A"
    ]
    print(f"Checking Sample 1: {sample_statements_1}")
    result1 = checker.check_contradictions(sample_statements_1)
    print(f"Contradiction found in Sample 1: {result1}\n")
    print(f"Checking Sample 2: {sample_statements_2}")
    result2 = checker.check_contradictions(sample_statements_2)
    print(f"Contradiction found in Sample 2: {result2}\n")
    print(f"Checking Sample 3: {sample_statements_3}")
    result3 = checker.check_contradictions(sample_statements_3)
    print(f"Contradiction found in Sample 3: {result3}\n")