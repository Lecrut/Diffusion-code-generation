def analyze_logic(conditions):
    parsed_conditions = []
    for condition in conditions:
        parts = condition.split(' if ')
        if len(parts) == 2 and all(part.strip() for part in parts):
            antecedent, consequent = parts
            parsed_conditions.append((antecedent.strip(), consequent.strip()))
        else:
            parsed_conditions.append((condition.strip(), "Malformed"))
    return parsed_conditions

def check_contradictions(conditions):
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

def are_mutually_exclusive(conditions_string):
    conditions = [c.strip() for c in conditions_string.split('if ') if c.strip()]
    parsed_conditions = analyze_logic(conditions)
    contradictions = check_contradictions(parsed_conditions)
    return bool(contradictions)

if __name__ == '__main__':
    sample_input = "if the sky is blue then the grass is green\nif the sky is not blue then the grass is not green"
    print(f"Are mutually exclusive: {are_mutually_exclusive(sample_input)}")