def analyze_logic(conditions_string):
    conditions = []
    parts = conditions_string.split('if ')
    for part in parts:
        if part:
            try:
                condition_str, consequence_str = part.split(' then ')
                condition = condition_str.strip()
                consequence = consequence_str.strip()
                conditions.append((condition, consequence))
            except ValueError:
                continue
    contradictions = []
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond_i, cons_i = conditions[i]
            cond_j, cons_j = conditions[j]
            if cond_i == cond_j:
                if cons_i != cons_j:
                    contradictions.append((f"Contradiction found between condition '{cond_i}' and '{cond_j}': Consequences differ. '{cons_i}' vs '{cons_j}'"))
    return contradictions
if __name__ == '__main__':
    sample_input = "if temperature is high then turn on AC if temperature is high then turn off AC if temperature is high then turn on AC"
    results = analyze_logic(sample_input)
    if results:
        print("Logical Contradictions Found:")
        for result in results:
            print(result)
    else:
        print("No logical contradictions found based on the simple heuristic.")