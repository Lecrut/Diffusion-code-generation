def check_contradictions(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond1 = conditions[i]
            cond2 = conditions[j]
            if are_contradictory(cond1, cond2):
                return True
    return False
def are_contradictory(cond1, cond2):
    if not cond1 or not cond2:
        return False
    dict1 = dict(cond1)
    dict2 = dict(cond2)
    common_keys = set(dict1.keys()) & set(dict2.keys())
    for key in common_keys:
        if dict1[key] != dict2[key]:
            return True
    return False
if __name__ == '__main__':
    sample_conditions = [
        (('color', 'red'), ('size', 'large')),
        (('color', 'blue'), ('size', 'small')),
        (('color', 'red'), ('size', 'small')),
        (('color', 'green'), ('size', 'large'))
    ]
    print(f"Sample Conditions: {sample_conditions}")
    result = check_contradictions(sample_conditions)
    print(f"Are there any contradictory conditions? {result}")
    sample_conditions_no_contradiction = [
        (('color', 'red'), ('size', 'large')),
        (('color', 'blue'), ('size', 'small')),
        (('color', 'green'), ('size', 'large'))
    ]
    print(f"\nSample Conditions (No Contradiction): {sample_conditions_no_contradiction}")
    result_no_contradiction = check_contradictions(sample_conditions_no_contradiction)
    print(f"Are there any contradictory conditions? {result_no_contradiction}")
    sample_conditions_contradiction = [
        (('color', 'red'), ('size', 'large')),
        (('color', 'red'), ('size', 'small'))
    ]
    print(f"\nSample Conditions (Contradiction): {sample_conditions_contradiction}")
    result_contradiction = check_contradictions(sample_conditions_contradiction)
    print(f"Are there any contradictory conditions? {result_contradiction}")