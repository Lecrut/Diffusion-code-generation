import itertools
class LogicChecker:
    def __init__(self, statements):
        self.statements = statements
    def check_contradictions(self):
        contradictions = []
        n = len(self.statements)
        for i in range(n):
            for j in range(i + 1, n):
                stmt1 = self.statements[i]
                stmt2 = self.statements[j]
                if stmt1 == stmt2:
                    continue
                if self._are_contradictory(stmt1, stmt2):
                    contradictions.append((i, j, stmt1, stmt2))
        return contradictions
    def _are_contradictory(self, s1, s2):
        if s1 == s2:
            return False
        if s1.startswith("not ") and s2.startswith("not "):
            return False
        if s1.startswith("not ") and s2.replace("not ", "") == s1.replace("not ", ""):
            return True
        if s2.startswith("not ") and s1.replace("not ", "") == s2.replace("not ", ""):
            return True
        return False
def parse_and_check(input_statements):
    parsed_statements = []
    for stmt in input_statements:
        parsed_statements.append(stmt.strip())
    checker = LogicChecker(parsed_statements)
    results = checker.check_contradictions()
    return results
if __name__ == '__main__':
    sample_statements = [
        "P",
        "not P",
        "Q",
        "not Q",
        "P",
        "Q"
    ]
    contradictions = parse_and_check(sample_statements)
    if contradictions:
        print("Contradictory pairs found:")
        for i, j, s1, s2 in contradictions:
            print(f"Statements at index {i} ('{s1}') and index {j} ('{s2}') are contradictory.")
    else:
        print("No logical contradictions found in the sample statements.")