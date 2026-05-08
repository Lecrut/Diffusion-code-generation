class LogicalContradictionChecker:
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
                    contradictions.append((f"Statement {i+1}: {stmt1}", f"Statement {j+1}: {stmt2}"))
        return contradictions
    def _are_contradictory(self, s1, s2):
        s1_parts = s1.lower().split(';')
        s2_parts = s2.lower().split(';')
        for p1 in s1_parts:
            if not p1.strip():
                continue
            for p2 in s2_parts:
                if not p2.strip():
                    continue
                if 'not ' in p1 and p1.startswith('not ' + p2):
                    return True
                if 'not ' in p2 and p2.startswith('not ' + p1):
                    return True
                if p1.strip() == p2.strip() and 'not' not in p1 and 'not' not in p2:
                    continue
        return False
if __name__ == '__main__':
    checker = LogicalContradictionChecker()
    statements_data = [
        "P is true",
        "not P is true",
        "Q is true",
        "not Q is true",
        "P is true; Q is false",
        "not (P is true)",
        "R is true"
    ]
    for stmt in statements_data:
        checker.add_statement(stmt)
    results = checker.check_contradictions()
    if results:
        print("Contradictions Found:")
        for contradiction in results:
            print(f"- {contradiction[0]} and {contradiction[1]}")
    else:
        print("No logical contradictions found based on the defined rules.")