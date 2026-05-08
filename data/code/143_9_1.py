import itertools
def parse_proposition(proposition):
    if proposition.startswith("if "):
        condition_str = proposition[3:].strip()
        if "then" in condition_str:
            antecedent_str, consequent_str = condition_str.split("then", 1)
            antecedent = antecedent_str.strip()
            consequent = consequent_str.strip()
            return {"type": "implication", "antecedent": antecedent, "consequent": consequent}
        else:
            return {"type": "simple", "proposition": condition_str}
    elif proposition.startswith("not "):
        proposition_str = proposition[4:].strip()
        return {"type": "negation", "proposition": proposition_str}
    else:
        return {"type": "atomic", "proposition": proposition}
def check_contradiction(statements):
    implications = []
    negations = []
    for stmt in statements:
        parsed = parse_proposition(stmt)
        if parsed["type"] == "implication":
            implications.append(parsed)
        elif parsed["type"] == "negation":
            negations.append(parsed)
        else:
            pass
    antecedents = set()
    consequents = set()
    for imp in implications:
        antecedents.add(imp["antecedent"])
        consequents.add(imp["consequent"])
    for imp1 in implications:
        for imp2 in implications:
            if imp1 is imp2:
                continue
            if imp1["antecedent"] == imp2["antecedent"]:
                if imp1["consequent"] == f"not {imp2['consequent']}" or imp2["consequent"] == f"not {imp1['consequent']}":
                    return True
    return False
if __name__ == '__main__':
    sample_statements = [
        "if P then Q",
        "if P then not Q",
        "if not P then Q",
        "if not P then not Q"
    ]
    is_contradictory = check_contradiction(sample_statements)
    print(f"Statements: {sample_statements}")
    print(f"Are the statements logically contradictory based on direct implication conflicts? {is_contradictory}")
    sample_statements_2 = [
        "if A then B",
        "if A then not B"
    ]
    is_contradictory_2 = check_contradiction(sample_statements_2)
    print(f"\nStatements: {sample_statements_2}")
    print(f"Are the statements logically contradictory based on direct implication conflicts? {is_contradictory_2}")
    sample_statements_3 = [
        "if P then Q",
        "if not P then not Q"
    ]
    is_contradictory_3 = check_contradiction(sample_statements_3)
    print(f"\nStatements: {sample_statements_3}")
    print(f"Are the statements logically contradictory based on direct implication conflicts? {is_contradictory_3}")