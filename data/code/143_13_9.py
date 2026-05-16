def analyze_logic(conditions):
    parsed_conditions = []
    for condition in conditions:
        parts = condition.split(' if ')
        if len(parts) == 2:
            condition_a = parts[0].strip()
            condition_b = parts[1].strip()
            parsed_conditions.append((condition_a, condition_b))
        elif len(parts) == 1:
            pass
    contradictions = []
    n = len(parsed_conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond_a_str, cond_b_str = parsed_conditions[i]
            cond_c_str, cond_d_str = parsed_conditions[j]
            if cond_a_str == cond_c_str and cond_b_str == cond_d_str:
                contradictions.append((i, j, "Identical conditions found"))
    return contradictions
if __name__ == '__main__':
    sample_string = "Condition A if B is true, Condition C if B is true, Condition D if B is true, Condition E if B is false"
    test_conditions = [
        "P if Q",
        "R if S",
        "P if Q",             
        "R if S",             
        "T if not Q"
    ]
    results = analyze_logic(test_conditions)
    if results:
        print("Logical Contradictions/Redundancies Found:")
        for i, j, reason in results:
            print(f"Indices ({i}, {j}): {reason}")
    else:
        print("No logical contradictions or redundancies found based on the implemented heuristic.")