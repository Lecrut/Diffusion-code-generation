def analyze_logic(conditions):
    parsed_conditions = []
    for condition_str in conditions:
        if "if" in condition_str and "then" in condition_str:
            parts = condition_str.split("if ", 1)
            if len(parts) > 1:
                antecedent, consequent = parts[1].split(" then", 1)
                parsed_conditions.append((antecedent.strip(), consequent.strip()))
    return parsed_conditions

def check_mutual_exclusivity(conditions):
    contradictions = []
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            antecedent_i, consequent_i = conditions[i]
            antecedent_j, consequent_j = conditions[j]

            if (antecedent_i == antecedent_j and consequent_i != consequent_j) or \
               (consequent_i == consequent_j and antecedent_i != antecedent_j):
                contradictions.append((conditions[i], conditions[j]))
    return contradictions

if __name__ == '__main__':
    sample_conditions = [
        "if the sky is blue then it is daytime",
        "if the sun rises in the east then it is morning",
        "if the moon is full then it is night"
    ]
    parsed_conditions = analyze_logic(sample_conditions)
    print("Parsed Conditions:", parsed_conditions)

    contradictions = check_mutual_exclusivity(parsed_conditions)
    print("Contradictions:", contradictions)