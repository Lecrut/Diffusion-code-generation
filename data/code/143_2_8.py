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
                if "and" in condition:
                    conditions = [c.strip() for c in condition.split("and")]
                    clauses.extend(conditions)
                elif "or" in condition:
                    conditions = [c.strip() for c in condition.split("or")]
                    clauses.extend(conditions)
                else:
                    clauses.append(condition)
                variables.update(set(condition.split("==")[0].strip()))
        all_conditions = []
        for clause in clauses:
            if "==" in clause:
                var1, var2 = clause.split("==")
                all_conditions.append((var1.strip(), var2.strip()))
            elif "==" in clause:
                var1, var2 = clause.split("==")
                all_conditions.append((var1.strip(), var2.strip()))
            else:
                all_conditions.append(clause)
        inferred_relations = set()
        for i in range(len(all_conditions)):
            for j in range(i + 1, len(all_conditions)):
                cond1 = all_conditions[i]
                cond2 = all_conditions[j]
                if isinstance(cond1, tuple) and isinstance(cond2, tuple):
                    v1a, v1b = cond1
                    v2a, v2b = cond2
                    if v1a == v2a and v1b != v2b:
                        return True
                    if v1a != v2a and v1b == v2b:
                        return True
                    if v1a == v2a and v1b != v2b:
                        return True
                    if v1a != v2a and v1b == v2b:
                        return True
                elif isinstance(cond1, str) and isinstance(cond2, str):
                    if cond1 == cond2 and cond1 != "":
                        return True
        return False
if __name__ == '__main__':
    checker = LogicChecker()
    statements1 = [
        "if A == B then C",
        "if B == C then A"
    ]
    print(f"Statements 1 Contradictory: {checker.analyze_statements(statements1)}")
    statements2 = [
        "if A == B then True",
        "if A != B then False"
    ]
    print(f"Statements 2 Contradictory: {checker.analyze_statements(statements2)}")
    statements3 = [
        "if A == B then True",
        "if B == C then True",
        "if A != C then False"
    ]
    print(f"Statements 3 Contradictory: {checker.analyze_statements(statements3)}")
    statements4 = [
        "if X == 1 then Y == 2"
    ]
    print(f"Statements 4 Contradictory: {checker.analyze_statements(statements4)}")
    statements5 = [
        "if P == Q and Q == R then S",
        "if P == R then S"
    ]
    print(f"Statements 5 Contradictory: {checker.analyze_statements(statements5)}")