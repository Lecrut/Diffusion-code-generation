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
            set1 = set(cond1)
            set2 = set(cond2)
            if not (set1 & set2):
                return True
    return False
if __name__ == '__main__':
    sample_conditions1 = [
        ('A', 'B'),
        ('C', 'D'),
        ('A', 'D')
    ]
    sample_conditions2 = [
        ('X', 'Y'),
        ('Y', 'Z'),
        ('X', 'Z')
    ]
    sample_conditions3 = [
        ('P', 'Q'),
        ('Q', 'R'),
        ('R', 'P')
    ]
    print(f"Sample 1 Contradictory: {check_contradictions(sample_conditions1)}")
    print(f"Sample 2 Contradictory: {check_contradictions(sample_conditions2)}")
    print(f"Sample 3 Contradictory: {check_contradictions(sample_conditions3)}")