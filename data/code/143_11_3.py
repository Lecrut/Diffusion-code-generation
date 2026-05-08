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
        s1_parts = s1.lower().split('not')
        s2_parts = s2.lower().split('not')
        if s1.startswith("not ") and s2.replace("not ", "").strip() == s1.replace("not ", "").strip():
            return False                                                            
        if s2.startswith("not ") and s1.replace("not ", "").strip() == s2.replace("not ", "").strip():
            return False                       
        if s1.startswith("not ") and s2.replace("not ", "").strip() == s1.replace("not ", "").strip():
            return True
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    statements1 = ["P", "Q", "R"]
    result1 = checker.check_contradictions(statements1)
    print(f"Statements: {statements1}")
    print(f"Contradictory: {result1}")
    print("-" * 20)
    statements2 = ["P", "not P", "Q"]
    result2 = checker.check_contradictions(statements2)
    print(f"Statements: {statements2}")
    print(f"Contradictory: {result2}")
    print("-" * 20)
    statements3 = ["P", "not P", "Q", "not Q"]
    result3 = checker.check_contradictions(statements3)
    print(f"Statements: {statements3}")
    print(f"Contradictory: {result3}")
    print("-" * 20)
    statements4 = ["P", "Q"]
    result4 = checker.check_contradictions(statements4)
    print(f"Statements: {statements4}")
    print(f"Contradictory: {result4}")
    print("-" * 20)
    statements5 = ["not P", "P"]
    result5 = checker.check_contradictions(statements5)
    print(f"Statements: {statements5}")
    print(f"Contradictory: {result5}")