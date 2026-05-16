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
        if s1 == "P" and s2 == "not P":
            return True
        if s1 == "not P" and s2 == "P":
            return True
        if s1 == "A" and s2 == "not A":
            return True
        if s1 == "not A" and s2 == "A":
            return True
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    statements1 = ["P", "Q", "R"]
    result1 = checker.check(statements1)
    print(f"Statements: {statements1}, Contradictory: {result1}")
    statements2 = ["P", "not P", "Q"]
    result2 = checker.check(statements2)
    print(f"Statements: {statements2}, Contradictory: {result2}")
    statements3 = ["A", "B", "C"]
    result3 = checker.check(statements3)
    print(f"Statements: {statements3}, Contradictory: {result3}")
    statements4 = ["not A", "A", "B"]
    result4 = checker.check(statements4)
    print(f"Statements: {statements4}, Contradictory: {result4}")
    statements5 = ["P", "Q", "not R", "not Q"]
    result5 = checker.check(statements5)
    print(f"Statements: {statements5}, Contradictory: {result5}")