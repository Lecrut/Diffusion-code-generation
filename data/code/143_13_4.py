def analyze_logic(conditions):
    parsed_conditions = []
    for condition_str in conditions:
        if condition_str.strip().startswith("if "):
            try:
                parts = condition_str.split("if ", 1)
                if len(parts) > 1:
                    condition = parts[1].strip()
                    parsed_conditions.append(condition)
            except Exception:
                continue
    return parsed_conditions
def check_contradictions(conditions):
    contradictions = []
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond1 = conditions[i]
            cond2 = conditions[j]
            if "and" in cond1 and "not" in cond2:
                contradictions.append((cond1, cond2, "Potential Negation Conflict"))
            elif "not" in cond1 and "and" in cond2:
                contradictions.append((cond1, cond2, "Potential Negation Conflict"))
            elif "true" in cond1 and "false" in cond2:
                contradictions.append((cond1, cond2, "Explicit Value Contradiction"))
            elif "false" in cond1 and "true" in cond2:
                contradictions.append((cond1, cond2, "Explicit Value Contradiction"))
    return contradictions
if __name__ == '__main__':
    sample_string = (
        "if temperature > 30 then alert_high\n"
        "if humidity < 50 then alert_dry\n"
        "if temperature > 30 and humidity < 50 then alert_critical\n"
        "if temperature > 30 then alert_low\n"
        "if humidity < 50 then not alert_dry"
    )
    conditions = analyze_logic(sample_string.split('\n'))
    contradictions = check_contradictions(conditions)
    if contradictions:
        print("Logical Contradictions Found:")
        for c1, c2, reason in contradictions:
            print(f"Conflict between: '{c1}' and '{c2}' -> Reason: {reason}")
    else:
        print("No obvious logical contradictions found based on simple keyword analysis.")