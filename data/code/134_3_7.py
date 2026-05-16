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
    set1 = set(cond1)
    set2 = set(cond2)
    intersection = set1.intersection(set2)
    for item in intersection:
        if len(item) == 2:
            attr1, val1 = item
            attr2, val2 = item
            if attr1 == attr2:
                if val1 != val2:
                    return True
    return False
if __name__ == '__main__':
    conditions1 = [
        (('color', 'red'), ('size', 'large')),
        (('color', 'blue'), ('size', 'small')),
        (('color', 'red'), ('size', 'small'))
    ]
    conditions2 = [
        (('color', 'red'), ('size', 'large')),
        (('color', 'red'), ('size', 'large'))
    ]
    conditions3 = [
        (('age', 30),),
        (('age', 40),)
    ]
    conditions4 = [
        (('type', 'A'),),
        (('type', 'B'),)
    ]
    print(f"Conditions 1 contradictory: {check_contradictions(conditions1)}")
    print(f"Conditions 2 contradictory: {check_contradictions(conditions2)}")
    print(f"Conditions 3 contradictory: {check_contradictions(conditions3)}")
    print(f"Conditions 4 contradictory: {check_contradictions(conditions4)}")