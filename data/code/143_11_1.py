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
        s1_lower = s1.lower().replace(" ", "")
        s2_lower = s2.lower().replace(" ", "")
        if s1_lower == s2_lower:
            return False
        if s1_lower.startswith("not") and s2_lower.replace("not", "") == s1_lower[3:]:
            return True
        if s2_lower.startswith("not") and s1_lower.replace("not", "") == s2_lower[3:]:
            return True
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    sample_statements_1 = [
        "P",
        "Q",
        "not P",
        "R"
    ]
    sample_statements_2 = [
        "A and B",
        "not (A and B)",
        "A"
    ]
    sample_statements_3 = [
        "T",
        "F"
    ]
    print(f"Test 1 (P, Q, not P, R): {checker.check(sample_statements_1)}")
    print(f"Test 2 (A and B, not (A and B), A): {checker.check(sample_statements_2)}")
    print(f"Test 3 (T, F): {checker.check(sample_statements_3)}")