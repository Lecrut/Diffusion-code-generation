import itertools
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
                if stmt1 == f"A and not B" and stmt2 == f"B" or stmt1 == f"B" and stmt2 == f"A and not B":
                    contradictions.append((stmt1, stmt2))
                elif stmt1 == "P" and stmt2 == "not P" or stmt1 == "not P" and stmt2 == "P":
                    contradictions.append((stmt1, stmt2))
                elif stmt1 == "True" and stmt2 == "False" or stmt1 == "False" and stmt2 == "True":
                    contradictions.append((stmt1, stmt2))
                elif stmt1 == "All are true" and stmt2 == "Some are false":
                    contradictions.append((stmt1, stmt2))
                elif stmt1 == "A is true" and stmt2 == "A is false":
                    contradictions.append((stmt1, stmt2))
                elif stmt1 == "X > 5" and stmt2 == "X < 3":
                    contradictions.append((stmt1, stmt2))
        return contradictions
if __name__ == '__main__':
    checker = LogicChecker()
    sample_statements = [
        "P",
        "not P",
        "True",
        "False",
        "X > 5",
        "X < 3",
        "All are true",
        "Some are false"
    ]
    for stmt in sample_statements:
        checker.add_statement(stmt)
    results = checker.check_contradictions()
    if results:
        print("Contradictory pairs found:")
        for s1, s2 in results:
            print(f"Statement 1: '{s1}' and Statement 2: '{s2}' are contradictory.")
    else:
        print("No logical contradictions found among the statements based on the defined rules.")