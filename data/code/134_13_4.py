def check_contradictions(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            set1 = set(conditions[i])
            set2 = set(conditions[j])
            if not set1.isdisjoint(set2):
                return True
    return False
if __name__ == '__main__':
    conditions1 = [
        (1, 2),
        (2, 3),
        (3, 4)
    ]
    conditions2 = [
        (1, 2),
        (3, 4)
    ]
    conditions3 = [
        (1, 2, 3),
        (2, 3, 4)
    ]
    conditions4 = [
        (1, 2),
        (3, 4),
        (1, 3)
    ]
    conditions5 = [
        (1, 2),
        (2, 3)
    ]
    print(f"Conditions 1: {check_contradictions(conditions1)}")
    print(f"Conditions 2: {check_contradictions(conditions2)}")
    print(f"Conditions 3: {check_contradictions(conditions3)}")
    print(f"Conditions 4: {check_contradictions(conditions4)}")
    print(f"Conditions 5: {check_contradictions(conditions5)}")