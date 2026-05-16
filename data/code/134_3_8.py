def check_contradictions(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond1 = conditions[i]
            cond2 = conditions[j]
            if cond1 == cond2:
                continue
            is_contradictory = False
            for c1, c2 in zip(cond1, cond2):
                if c1 == 'A' and c2 == 'B':
                    is_contradictory = True
                    break
                if c1 == 'B' and c2 == 'A':
                    is_contradictory = True
                    break
                if c1 == 'X' and c2 == 'Y':
                    is_contradictory = True
                    break
                if c1 == 'Y' and c2 == 'X':
                    is_contradictory = True
                    break
            if is_contradictory:
                return True
    return False
if __name__ == '__main__':
    sample_conditions_1 = [
        (('A', 'B'), ('C', 'D')),
        (('E', 'F'), ('G', 'H'))
    ]
    sample_conditions_2 = [
        (('A', 'B'), ('B', 'A')),
        (('X', 'Y'), ('Y', 'X'))
    ]
    sample_conditions_3 = [
        (('A', 'B'), ('B', 'A')),
        (('X', 'Y'), ('Z', 'W'))
    ]
    sample_conditions_4 = [
        (('A', 'B'), ('B', 'A')),
        (('A', 'B'), ('B', 'A'))
    ]
    print(f"Sample 1 Contradictory: {check_contradictions(sample_conditions_1)}")
    print(f"Sample 2 Contradictory: {check_contradictions(sample_conditions_2)}")
    print(f"Sample 3 Contradictory: {check_contradictions(sample_conditions_3)}")
    print(f"Sample 4 Contradictory: {check_contradictions(sample_conditions_4)}")