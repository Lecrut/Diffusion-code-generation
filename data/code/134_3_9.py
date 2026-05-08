def check_contradictions(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond1 = conditions[i]
            cond2 = conditions[j]
            if cond1 == cond2:
                continue
            is_contradictory = False
            if cond1 == cond2:
                is_contradictory = True
            if is_contradictory:
                return True
    return False
if __name__ == '__main__':
    sample_conditions_1 = [
        (1, 'A', 5),
        (2, 'B', 10),
        (1, 'A', 5)
    ]
    sample_conditions_2 = [
        (1, 'A', 5),
        (2, 'B', 10),
        (1, 'A', 5),
        (3, 'C', 15)
    ]
    sample_conditions_3 = [
        (1, 'A', 5),
        (1, 'A', 5)
    ]
    print(f"Sample 1 Contradictory: {check_contradictions(sample_conditions_1)}")
    print(f"Sample 2 Contradictory: {check_contradictions(sample_conditions_2)}")
    print(f"Sample 3 Contradictory: {check_contradictions(sample_conditions_3)}")