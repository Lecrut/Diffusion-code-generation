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
            parsed_conditions.append(("Empty", "Empty"))
    return parsed_conditions
def check_contradictions(parsed_conditions):
    contradictions = []
    n = len(parsed_conditions)
    for i in range(n):
        for j in range(i + 1, n):
            antecedent_i, consequent_i = parsed_conditions[i]
            antecedent_j, consequent_j = parsed_conditions[j]
            if antecedent_i == antecedent_j:
                if consequent_i != consequent_j:
                    contradictions.append((f"Conflict between {i} and {j}: Antecedent '{antecedent_i}' implies different consequents ('{consequent_i}' vs '{consequent_j}')"))
    return contradictions
if __name__ == '__main__':
    sample_string = (
        "if temperature > 30 then alert_high if humidity < 50 else alert_medium if humidity >= 50 if time_of_day == 'night' then alert_critical"
    )
    parsed = analyze_logic(sample_string.split(' if '))
    print("--- Parsed Conditions ---")
    for a, c in parsed:
        print(f"Antecedent: '{a}', Consequent: '{c}'")
    contradictions = check_contradictions(parsed)
    print("\n--- Logical Contradictions Found ---")
    if contradictions:
        for c in contradictions:
            print(c)
    else:
        print("No direct logical contradictions found based on the simple pairwise check.")