import re
def analyze_logic(conditions):
    parsed_conditions = []
    for cond in conditions:
        match = re.match(r"^\s*if\s+(.*)\s*:\s*(.*)$", cond.strip())
        if match:
            condition_text = match.group(1).strip()
            result_text = match.group(2).strip()
            parsed_conditions.append((condition_text, result_text))
        else:
            pass
    return parsed_conditions
def check_contradictions(parsed_conditions):
    contradictions = []
    if len(parsed_conditions) < 2:
        return contradictions
    for i in range(len(parsed_conditions)):
        for j in range(i + 1, len(parsed_conditions)):
            cond1, res1 = parsed_conditions[i]
            cond2, res2 = parsed_conditions[j]
            if cond1 == cond2 and res1 != res2:
                contradictions.append(f"Contradiction found between condition {i+1} and {j+1}: Premise '{cond1}' yields different results ('{res1}' vs '{res2}')")
    return contradictions
if __name__ == '__main__':
    sample_string = (
        "if temperature > 30: result is hot\n"
        "if temperature > 25: result is warm\n"
        "if temperature > 30: result is cold\n"
        "if temperature > 25: result is hot"
    )
    conditions = sample_string.split('\n')
    parsed = analyze_logic(conditions)
    results = check_contradictions(parsed)
    if results:
        print("Logical Contradictions Detected:")
        for res in results:
            print(res)
    else:
        print("No inherent logical contradictions found based on structural analysis.")