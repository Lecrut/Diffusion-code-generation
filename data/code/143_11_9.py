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
        s1_lower = s1.lower().strip()
        s2_lower = s2.lower().strip()
        if s1_lower.startswith("not ") and s2_lower.replace("not ", "") == s1_lower.replace("not ", ""):
            return True
        if s2_lower.startswith("not ") and s1_lower.replace("not ", "") == s2_lower.replace("not ", ""):
            return True
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    statements1 = [
        "P",
        "Q",
        "R"
    ]
    print(f"Statements 1: {statements1}")
    print(f"Contradictory: {checker.check_contradictions(statements1)}\n")
    statements2 = [
        "P",
        "not P",
        "Q"
    ]
    print(f"Statements 2: {statements2}")
    print(f"Contradictory: {checker.check_contradictions(statements2)}\n")
    statements3 = [
        "P",
        "Q"
    ]
    print(f"Statements 3: {statements3}")
    print(f"Contradictory: {checker.check_contradictions(statements3)}\n")
    statements4 = [
        "A",
        "A"
    ]
    print(f"Statements 4: {statements4}")
    print(f"Contradictory: {checker.check_contradictions(statements4)}\n")
    statements5 = [
        "A",
        "not A",
        "B"
    ]
    print(f"Statements 5: {statements5}")
    print(f"Contradictory: {checker.check_contradictions(statements5)}\n")