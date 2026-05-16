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
                contradictions.append((i, j, f"Contradictory implications: {antecedent_i} implies {consequent_i} and {antecedent_j} implies {consequent_j}"))
    return contradictions
if __name__ == '__main__':
    sample_string = "if temperature is high then fan should be on if temperature is low then fan should be off if temperature is high then fan should be off"
    conditions_list = sample_string.split(' if ')
    results = analyze_logic(conditions_list)
    if results:
        print("Logical Contradictions Found:")
        for i, j, reason in results:
            print(f"Indices ({i}, {j}): {reason}")
    else:
        print("No inherent logical contradictions found based on simple implication checking.")