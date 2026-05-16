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
                print(f"Contradiction found between condition {i} and condition {j}: {cond1} and {cond2}")
                pass
    return False
if __name__ == '__main__':
    sample_conditions = [
        (1, 2, 'A'),
        (3, 4, 'B'),
        (1, 2, 'A'),
        (5, 6, 'C')
    ]
    print("--- Test Case 1: Identical Conditions ---")
    result1 = check_contradictions(sample_conditions)
    print(f"Contradictions found: {result1}\n")
    sample_conditions_2 = [
        (1, 10),
        (5, 15),
        (1, 10)
    ]
    print("--- Test Case 2: Identical Conditions ---")
    result2 = check_contradictions(sample_conditions_2)
    print(f"Contradictions found: {result2}\n")
    sample_conditions_3 = [
        (1, 2),
        (3, 4),
        (1, 2)
    ]
    print("--- Test Case 3: Mixed Conditions ---")
    result3 = check_contradictions(sample_conditions_3)
    print(f"Contradictions found: {result3}\n")