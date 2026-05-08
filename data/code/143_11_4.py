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
        s1_lower = s1.lower().replace(" ", "")
        s2_lower = s2.lower().replace(" ", "")
        if "not" in s1 and s2.startswith("not"):
            if s1.startswith("not "):
                prop1 = s1[4:].strip()
                if s2 == prop1:
                    return True
            elif s2.startswith("not "):
                prop2 = s2[4:].strip()
                if s1 == prop2:
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
    result_1 = checker.check_contradictions(sample_statements_1)
    print(f"Statements 1: {sample_statements_1}")
    print(f"Contradiction found in Set 1: {result_1}")
    sample_statements_2 = [
        "A and B",
        "not (A and B)",
        "A"
    ]
    result_2 = checker.check_contradictions(sample_statements_2)
    print(f"\nStatements 2: {sample_statements_2}")
    print(f"Contradiction found in Set 2: {result_2}")
    sample_statements_3 = [
        "True",
        "False",
        "True"
    ]
    result_3 = checker.check_contradictions(sample_statements_3)
    print(f"\nStatements 3: {sample_statements_3}")
    print(f"Contradiction found in Set 3: {result_3}")
    sample_statements_4 = [
        "P",
        "not P",
        "Q"
    ]
    result_4 = checker.check_contradictions(sample_statements_4)
    print(f"\nStatements 4: {sample_statements_4}")
    print(f"Contradiction found in Set 4: {result_4}")