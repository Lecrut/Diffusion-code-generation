def check_contradictory_conditions(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond1 = conditions[i]
            cond2 = conditions[j]
            if not are_contradictory(cond1, cond2):
                continue
            else:
                return True
    return False
def are_contradictory(cond1, cond2):
    if not cond1 or not cond2:
        return False
    attributes1 = {attr: val for attr, val in cond1}
    attributes2 = {attr: val for attr, val in cond2}
    all_attributes = set(attributes1.keys()) | set(attributes2.keys())
    for attr in all_attributes:
        val1 = attributes1.get(attr)
        val2 = attributes2.get(attr)
        if val1 is not None and val2 is not None and val1 != val2:
            return True
    return False
if __name__ == '__main__':
    sample_conditions = [
        (('color', 'red'), ('size', 'large')),
        (('color', 'blue'), ('size', 'small')),
        (('color', 'red'), ('size', 'small')),
        (('color', 'green'), ('size', 'large'))
    ]
    print(f"Checking sample conditions: {sample_conditions}")
    result1 = check_contradictory_conditions(sample_conditions)
    print(f"Are there contradictory conditions in sample 1? {result1}")
    sample_conditions_2 = [
        (('color', 'red'), ('size', 'large')),
        (('color', 'red'), ('size', 'large'))
    ]
    print(f"\nChecking sample conditions: {sample_conditions_2}")
    result2 = check_contradictory_conditions(sample_conditions_2)
    print(f"Are there contradictory conditions in sample 2? {result2}")
    sample_conditions_3 = [
        (('color', 'red'), ('size', 'large')),
        (('color', 'blue'), ('size', 'small')),
        (('color', 'green'), ('size', 'medium'))
    ]
    print(f"\nChecking sample conditions: {sample_conditions_3}")
    result3 = check_contradictory_conditions(sample_conditions_3)
    print(f"Are there contradictory conditions in sample 3? {result3}")