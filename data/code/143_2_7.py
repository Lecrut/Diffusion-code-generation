class LogicChecker:
    def analyze_statements(self, statements):
        variables = set()
        clauses = []
        for statement in statements:
            parts = statement.split(' if ')
            if len(parts) != 2:
                continue
            condition = parts[0].strip()
            consequence = parts[1].strip()
            condition_vars = set()
            consequence_vars = set()
            for var in condition.split(' and '):
                condition_vars.add(var.strip())
            for var in consequence.split(' and '):
                consequence_vars.add(var.strip())
            variables.update(condition_vars)
            variables.update(consequence_vars)
            clauses.append((condition_vars, consequence_vars))
        contradictory = False
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                cond1_vars, cons1_vars = clauses[i]
                cond2_vars, cons2_vars = clauses[j]
                intersection = cond1_vars.intersection(cons2_vars)
                if intersection:
                    contradictory = True
                    break
            if contradictory:
                break
        return contradictory
if __name__ == '__main__':
    checker = LogicChecker()
    sample_statements_1 = [
        "if P and Q then R",
        "if R then not P"
    ]
    result_1 = checker.analyze_statements(sample_statements_1)
    print(f"Sample 1 Contradictory: {result_1}")
    sample_statements_2 = [
        "if P then Q",
        "if Q then R",
        "if R then P"
    ]
    result_2 = checker.analyze_statements(sample_statements_2)
    print(f"Sample 2 Contradictory: {result_2}")
    sample_statements_3 = [
        "if P then Q",
        "if P then not Q"
    ]
    result_3 = checker.analyze_statements(sample_statements_3)
    print(f"Sample 3 Contradictory: {result_3}")
    sample_statements_4 = [
        "if A then B",
        "if C then D"
    ]
    result_4 = checker.analyze_statements(sample_statements_4)
    print(f"Sample 4 Contradictory: {result_4}")
    sample_statements_5 = [
        "if P then Q",
        "if Q then not P"
    ]
    result_5 = checker.analyze_statements(sample_statements_5)
    print(f"Sample 5 Contradictory: {result_5}")