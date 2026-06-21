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
                raise ValueError(f"Malformed condition: {condition}")
        else:
            raise ValueError("Empty condition")
    contradictions = []
    n = len(parsed_conditions)
    for i in range(n):
        for j in range(i + 1, n):
            antecedent_i, consequent_i = parsed_conditions[i]
            antecedent_j, consequent_j = parsed_conditions[j]
            if antecedent_i == antecedent_j and consequent_i != consequent_j:
                contradictions.append((antecedent_i, consequent_i, consequent_j))
    return contradictions

if __name__ == '__main__':
    sample_conditions = [
        "it is raining if the sky is gray",
        "it is not raining if the sky is blue",
        "it is sunny if it is daytime"
    ]
    try:
        result = analyze_logic(sample_conditions)
        print(result)
    except ValueError as e:
        print(e)