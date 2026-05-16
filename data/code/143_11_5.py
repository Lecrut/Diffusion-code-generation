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
        s1_norm = s1.lower().replace(" and ", " ").replace(" or ", " ").replace(" not ", " ~")
        s2_norm = s2.lower().replace(" and ", " ").replace(" or ", " ").replace(" not ", " ~")
        if s1_norm == "~" + s2_norm or s2_norm == "~" + s1_norm:
            return True
        if s1.strip() == s2.strip() and "not" in s1.lower() and "not" in s2.lower():
             pass
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    statements1 = [
        "P",
        "Q",
        "P or Q"
    ]
    result1 = checker.check(statements1)
    print(f"Statements 1: {statements1}")
    print(f"Contradictory: {result1}")
    print("-" * 20)
    statements2 = [
        "P",
        "not P"
    ]
    result2 = checker.check(statements2)
    print(f"Statements 2: {statements2}")
    print(f"Contradictory: {result2}")
    print("-" * 20)
    statements3 = [
        "A is true",
        "B is true"
    ]
    result3 = checker.check(statements3)
    print(f"Statements 3: {statements3}")
    print(f"Contradictory: {result3}")
    print("-" * 20)
    statements4 = [
        "P",
        "not P"
    ]
    result4 = checker.check(statements4)
    print(f"Statements 4: {statements4}")
    print(f"Contradictory: {result4}")
    print("-" * 20)
    statements5 = [
        "P",
        "P"
    ]
    result5 = checker.check(statements5)
    print(f"Statements 5: {statements5}")
    print(f"Contradictory: {result5}")