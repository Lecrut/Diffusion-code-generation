def check_contradictions(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond1 = conditions[i]
            cond2 = conditions[j]
            if cond1 == cond2:
                continue
            is_contradictory = False
            if cond1[0] != cond2[0]:
                is_contradictory = True
            elif cond1[0] == cond2[0]:
                if len(cond1) > 1 and cond1[1] != cond2[1]:
                    is_contradictory = True
                elif len(cond1) == 1 and len(cond2) == 1 and cond1[0] != cond2[0]:
                    is_contradictory = True
            if is_contradictory:
                return True
    return False
if __name__ == '__main__':
    sample_conditions_1 = [
        ("color", "red"),
        ("shape", "square"),
        ("color", "blue")
    ]
    sample_conditions_2 = [
        ("type", "A", 10),
        ("type", "B", 20),
        ("type", "A", 15)
    ]
    sample_conditions_3 = [
        ("color", "red"),
        ("shape", "square"),
        ("color", "red")
    ]
    print(f"Sample 1 Contradictory: {check_contradictions(sample_conditions_1)}")
    print(f"Sample 2 Contradictory: {check_contradictions(sample_conditions_2)}")
    print(f"Sample 3 Contradictory: {check_contradictions(sample_conditions_3)}")