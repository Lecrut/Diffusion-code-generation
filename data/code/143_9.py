import itertools
def parse_proposition(proposition_str):
    if proposition_str.startswith("IF"):
        return "IF_" + proposition_str[2:].strip()
    elif proposition_str.startswith("NOT"):
        return "NOT_" + proposition_str[3:].strip()
    elif proposition_str.startswith("THEN"):
        return "THEN_" + proposition_str[4:].strip()
    else:
        return proposition_str
def evaluate_implication(antecedent, consequent):
    if antecedent.startswith("IF_") and consequent.startswith("THEN_"):
        antecedent_val = int(antecedent.split('_')[1])
        consequent_val = int(consequent.split('_')[1])
        return antecedent_val <= consequent_val
    return False
def check_contradiction(premises):
    if not premises:
        return False
    all_implications = []
    for p in premises:
        parts = p.split(":")
        if len(parts) == 2:
            antecedent = parts[0].strip()
            consequent = parts[1].strip()
            all_implications.append((antecedent, consequent))
    if not all_implications:
        return False
    for i in range(len(all_implications)):
        for j in range(i + 1, len(all_implications)):
            antecedent1, consequent1 = all_implications[i]
            antecedent2, consequent2 = all_implications[j]
            if antecedent1 == antecedent2:
                if consequent1 != consequent2:
                    return True
    return False
if __name__ == '__main__':
    sample_premises = [
        "IF 1 THEN 0",
        "IF 1 THEN 1",
        "IF 2 THEN 3"
    ]
    print(f"Premises: {sample_premises}")
    is_contradictory = check_contradiction(sample_premises)
    print(f"Are the premises contradictory? {is_contradictory}")
    contradictory_premises = [
        "IF 1 THEN 0",
        "IF 1 THEN 1"
    ]
    print(f"\nContradictory Premises Test: {contradictory_premises}")
    is_contradictory_test = check_contradiction(contradictory_premises)
    print(f"Are the contradictory premises contradictory? {is_contradictory_test}")