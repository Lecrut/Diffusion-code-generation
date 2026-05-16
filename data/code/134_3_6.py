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
    sample_conditions = [
        (1, 2, 'A'),
        (3, 4, 'B'),
        (1, 2, 'A'),
        (5, 6, 'C')
    ]
    result1 = check_contradictions(sample_conditions)
    print(f"Sample 1 Contradictory: {result1}")
    sample_conditions_2 = [
        (1, 2, 'A'),
        (3, 4, 'B'),
        (1, 2, 'B')
    ]
    result2 = check_contradictions(sample_conditions_2)
    print(f"Sample 2 Contradictory: {result2}")
    sample_conditions_3 = [
        (1, 2, 'A'),
        (3, 4, 'B'),
        (5, 6, 'C')
    ]
    result3 = check_contradictions(sample_conditions_3)
    print(f"Sample 3 Contradictory: {result3}")