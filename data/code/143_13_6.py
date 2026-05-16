def analyze_logic(conditions):
    parsed_conditions = []
    for condition in conditions:
        if condition.strip():
            parts = condition.split(' if ')
            if len(parts) == 2:
                antecedent = parts[0].strip()
                consequent = parts[1].strip()
                parsed_conditions.append((antecedent, consequent))
            else:
                parsed_conditions.append((condition, "Malformed"))
        else:
            parsed_conditions.append((condition, "Empty"))
    contradictions = []
    n = len(parsed_conditions)
    for i in range(n):
        for j in range(i + 1, n):
            antecedent_i, consequent_i = parsed_conditions[i]
            antecedent_j, consequent_j = parsed_conditions[j]
            if antecedent_i == antecedent_j and consequent_i != consequent_j:
                contradictions.append((i, j, f"Contradictory: {antecedent_i} implies {consequent_i} and {consequent_j}"))
    return contradictions
if __name__ == '__main__':
    sample_string = (
        "if temperature > 30 then alert=True if humidity < 50 else alert=False if time > 18 then action=Night else action=Day"
    )
    raw_statements = [
        "temperature > 30 then alert=True",
        "humidity < 50 then alert=False",
        "time > 18 then action=Night",
        "time <= 18 then action=Day"
    ]
    test_conditions = [
        "temperature > 30 if humidity < 50",
        "temperature > 30 if humidity >= 50",
        "time > 18 if action=Night",
        "time <= 18 if action=Day"
    ]
    results = analyze_logic(test_conditions)
    if results:
        print("Logical Contradictions Found:")
        for i, j, reason in results:
            print(f"Pair ({i}, {j}): {reason}")
    else:
        print("No inherent logical contradictions found based on the defined criteria.")