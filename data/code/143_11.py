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
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    statements1 = [
        "P",
        "Q",
        "R"
    ]
    result1 = checker.check(statements1)
    print(f"Statements 1: {statements1}")
    print(f"Contradiction found: {result1}")
    print("-" * 20)
    statements2 = [
        "P",
        "~P"
    ]
    result2 = checker.check(statements2)
    print(f"Statements 2: {statements2}")
    print(f"Contradiction found: {result2}")
    print("-" * 20)
    statements3 = [
        "P",
        "Q"
    ]
    result3 = checker.check(statements3)
    print(f"Statements 3: {statements3}")
    print(f"Contradiction found: {result3}")
    print("-" * 20)
    statements4 = [
        "P",
        "P"
    ]
    result4 = checker.check(statements4)
    print(f"Statements 4: {statements4}")
    print(f"Contradiction found: {result4}")
    print("-" * 20)
    statements5 = [
        "A",
        "~A",
        "B"
    ]
    result5 = checker.check(statements5)
    print(f"Statements 5: {statements5}")
    print(f"Contradiction found: {result5}")