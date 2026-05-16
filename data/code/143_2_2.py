class LogicChecker:
    def analyze_statements(self, statements):
        variables = set()
        clauses = []
        for statement in statements:
            if "if" in statement:
                parts = statement.split("if")
                condition_str = parts[1].strip()
                if "then" in condition_str:
                    condition, consequence = condition_str.split("then", 1)
                    condition = condition.strip()
                    consequence = consequence.strip()
                else:
                    condition = condition_str
                    consequence = None
                condition_parts = [p.strip() for p in condition.split("and")]
                for part in condition_parts:
                    if part:
                        variables.add(part)
                if consequence:
                    consequence_parts = [p.strip() for p in consequence.split("then")]
                    for part in consequence_parts:
                        if part:
                            variables.add(part)
        if not variables:
            return False
        contradictions = set()
        for var in variables:
            true_assignments = set()
            false_assignments = set()
            for stmt in statements:
                if "if" in stmt:
                    condition_str = stmt.split("if")[1].strip()
                    if "and" in condition_str:
                        parts = [p.strip() for p in condition_str.split("and")]
                        for part in parts:
                            if part.startswith(var) and part.startswith("not"):
                                if var in false_assignments:
                                    contradictions.add(f"{var} is contradictory")
                                    break
                            elif part.startswith(var):
                                true_assignments.add(var)
                            elif part.startswith("not"):
                                false_assignments.add(var)
            if true_assignments and false_assignments:
                contradictions.add(f"{var} has conflicting assignments")
        return len(contradictions) > 0
if __name__ == '__main__':
    checker = LogicChecker()
    sample_statements_1 = [
        "if A and B then C",
        "if A then not A"
    ]
    print(f"Sample 1 Contradictory: {checker.analyze_statements(sample_statements_1)}")
    sample_statements_2 = [
        "if A then B",
        "if B then C"
    ]
    print(f"Sample 2 Contradictory: {checker.analyze_statements(sample_statements_2)}")
    sample_statements_3 = [
        "if A then B",
        "if not B then not A"
    ]
    print(f"Sample 3 Contradictory: {checker.analyze_statements(sample_statements_3)}")
    sample_statements_4 = [
        "if A then B",
        "if A then not B"
    ]
    print(f"Sample 4 Contradictory: {checker.analyze_statements(sample_statements_4)}")
    sample_statements_5 = [
        "if P then Q",
        "if not P then not Q"
    ]
    print(f"Sample 5 Contradictory: {checker.analyze_statements(sample_statements_5)}")