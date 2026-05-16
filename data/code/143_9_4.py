import itertools
def parse_proposition(proposition_str):
    parts = proposition_str.split('->')
    if len(parts) == 2:
        antecedent = proposition_str.split('->')[0].strip()
        consequent = proposition_str.split('->')[1].strip()
        return (antecedent, consequent)
    return None
def check_contradiction(implications):
    if not implications:
        return False
    all_antecedents = [imp[0] for imp in implications]
    all_consequents = [imp[1] for imp in implications]
    for a, b in itertools.combinations(all_antecedents, 2):
        for c, d in itertools.combinations(all_consequents, 2):
            if a == b:
                continue
            if c == d:
                continue
            if (a == c and b == d):
                return True
    return False
if __name__ == '__main__':
    sample_implications = [
        "P -> Q",
        "Q -> R",
        "R -> P"
    ]
    print(f"Implications: {sample_implications}")
    is_contradictory = check_contradiction(sample_implications)
    print(f"Are the implications contradictory? {is_contradictory}")