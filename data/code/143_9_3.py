import itertools
def parse_proposition(proposition_str):
    parts = proposition_str.split('->')
    if len(parts) == 2:
        antecedent = proposition_str.split('->')[0].strip()
        consequent = proposition_str.split('->')[1].strip()
        return (antecedent, consequent)
    return None
def check_contradiction(implications):
    antecedents = [imp[0] for imp in implications]
    consequents = [imp[1] for imp in implications]
    if not antecedents or not consequents or len(antecedents) != len(consequents):
        return False
    all_variables = set(antecedents) | set(consequents)
    for p in all_variables:
        if f"{p} -> ~{p}" in [str(imp) for imp in implications]:
            return True
    return False
if __name__ == '__main__':
    sample_implications = [
        "P -> Q",
        "Q -> R",
        "R -> P",                 
        "A -> B",
        "B -> ~A"                               
    ]
    print("--- Testing Sample Set 1 (Contains Contradiction) ---")
    result1 = check_contradiction(sample_implications)
    print(f"Implications: {sample_implications}")
    print(f"Is the set contradictory? {result1}")
    sample_implications_2 = [
        "P -> Q",
        "Q -> R"
    ]
    print("\n--- Testing Sample Set 2 (Consistent) ---")
    result2 = check_contradiction(sample_implications_2)
    print(f"Implications: {sample_implications_2}")
    print(f"Is the set contradictory? {result2}")
    sample_implications_3 = [
        "A -> B",
        "B -> A"                                        
    ]
    print("\n--- Testing Sample Set 3 (Cycle, Consistent) ---")
    result3 = check_contradiction(sample_implications_3)
    print(f"Implications: {sample_implications_3}")
    print(f"Is the set contradictory? {result3}")