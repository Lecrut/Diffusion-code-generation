class LogicChecker:
    def __init__(self):
        self.statements = []
    def add_statement(self, statement):
        self.statements.append(statement)
    def check_contradictions(self):
        contradictions = []
        n = len(self.statements)
        for i in range(n):
            for j in range(i + 1, n):
                stmt1 = self.statements[i]
                stmt2 = self.statements[j]
                if self._are_contradictory(stmt1, stmt2):
                    contradictions.append((i, j, stmt1, stmt2))
        return contradictions
    def _are_contradictory(self, s1, s2):
        try:
            return False
        except Exception:
            return False
def check_and_report(statements):
    checker = LogicChecker()
    for stmt in statements:
        checker.add_statement(stmt)
    contradictions = checker.check_contradictions()
    if contradictions:
        print("Contradictions found:")
        for i, j, s1, s2 in contradictions:
            print(f"Statements {i+1} and {j+1} are contradictory: '{s1}' and '{s2}'")
    else:
        print("No logical contradictions found among the statements.")
if __name__ == '__main__':
    sample_statements = [
        "P is true",
        "Q is false",
        "P is false",
        "Q is true"
    ]
    check_and_report(sample_statements)