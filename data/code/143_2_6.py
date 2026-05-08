class LogicChecker:
    def analyze_statements(self, statements):
        positive_conditions = set()
        negative_conditions = set()
        for statement in statements:
            if "and" in statement:
                parts = statement.split("and")
                for part in parts:
                    if part.strip().startswith("if"):
                        condition = part.split("if")[1].strip()
                        if "not" in condition:
                            negative_conditions.add(condition)
                        else:
                            positive_conditions.add(condition)
            elif "or" in statement:
                parts = statement.split("or")
                for part in parts:
                    if part.strip().startswith("if"):
                        condition = part.split("if")[1].strip()
                        if "not" in condition:
                            negative_conditions.add(condition)
                        else:
                            positive_conditions.add(condition)
            elif statement.startswith("if"):
                condition = statement.split("if")[1].strip()
                if "not" in condition:
                    negative_conditions.add(condition)
                else:
                    positive_conditions.add(condition)
        contradiction_found = False
        for pos in positive_conditions:
            for neg in negative_conditions:
                if pos == neg:
                    contradiction_found = True
                    break
            if contradiction_found:
                break
        return contradiction_found
if __name__ == '__main__':
    checker = LogicChecker()
    sample1 = [
        "if A then B",
        "if B then not A"
    ]
    result1 = checker.analyze_statements(sample1)
    print(f"Sample 1 Contradictory: {result1}")
    sample2 = [
        "if A then B",
        "if B then C"
    ]
    result2 = checker.analyze_statements(sample2)
    print(f"Sample 2 Contradictory: {result2}")
    sample3 = [
        "if A then B",
        "if not B then not A"
    ]
    result3 = checker.analyze_statements(sample3)
    print(f"Sample 3 Contradictory: {result3}")
    sample4 = [
        "if A then B",
        "if not A then not B"
    ]
    result4 = checker.analyze_statements(sample4)
    print(f"Sample 4 Contradictory: {result4}")
    sample5 = [
        "if A then B",
        "if not A then B"
    ]
    result5 = checker.analyze_statements(sample5)
    print(f"Sample 5 Contradictory: {result5}")