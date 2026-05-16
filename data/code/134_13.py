def check_contradictions(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            set1 = set(conditions[i])
            set2 = set(conditions[j])
            if set1.intersection(set2):
                return True
    return False
if __name__ == '__main__':
    conditions1 = [
        (1, 2),
        (2, 3),
        (4, 5)
    ]
    conditions2 = [
        (1, 2, 3),
        (2, 3, 4),
        (3, 4, 5)
    ]
    conditions3 = [
        (1, 2),
        (2, 3)
    ]
    conditions4 = [
        (1, 2),
        (2, 1)
    ]
    print(f"Conditions 1: {check_contradictions(conditions1)}")
    print(f"Conditions 2: {check_contradictions(conditions2)}")
    print(f"Conditions 3: {check_contradictions(conditions3)}")
    print(f"Conditions 4: {check_contradictions(conditions4)}")