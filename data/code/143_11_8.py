class ContradictionChecker:
    def check(self, statements):
        n = len(statements)
        for i in range(n):
            for j in range(i + 1, n):
                s1 = statements[i]
                s2 = statements[j]
                if self._are_contradictory(s1, s2):
                    return True
        return False
    def _are_contradictory(self, s1, s2):
        if s1.startswith("not ") and s2.strip("not ") == s1[4:]:
            return True
        if s2.startswith("not ") and s1.strip("not ") == s2[4:]:
            return True
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    statements1 = [
        "P",
        "Q",
        "P OR Q"
    ]
    result1 = checker.check(statements1)
    print(f"Statements 1: {statements1}")
    print(f"Contradictory: {result1}")
    print("-" * 20)
    statements2 = [
        "P",
        "not P",
        "Q"
    ]
    result2 = checker.check(statements2)
    print(f"Statements 2: {statements2}")
    print(f"Contradictory: {result2}")
    print("-" * 20)
    statements3 = [
        "A",
        "B",
        "not A"
    ]
    result3 = checker.check(statements3)
    print(f"Statements 3: {statements3}")
    print(f"Contradictory: {result3}")
    print("-" * 20)
    statements4 = [
        "P",
        "Q",
        "not P"
    ]
    result4 = checker.check(statements4)
    print(f"Statements 4: {statements4}")
    print(f"Contradictory: {result4}")