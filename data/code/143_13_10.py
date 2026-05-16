import re
def analyze_logic(conditions):
    parsed_conditions = []
    for condition in conditions:
        match = re.match(r"^(.*)\s+if\s+(.*)$", condition.strip())
        if match:
            statement = match.group(1).strip()
            condition_str = match.group(2).strip()
            parsed_conditions.append({
                "statement": statement,
                "condition": condition_str
            })
        else:
            parsed_conditions.append({"error": "Invalid format", "original": condition})
    contradictions = []
    n = len(parsed_conditions)
    for i in range(n):
        for j in range(i + 1, n):
            cond_i = parsed_conditions[i]
            cond_j = parsed_conditions[j]
            if "error" in cond_i or "error" in cond_j:
                continue
            if "not" in cond_i["condition"].lower() and cond_j["condition"].lower().startswith("not "):
                contradictions.append(f"Potential contradiction between '{cond_i['statement']}' and '{cond_j['statement']}'")
    return contradictions
if __name__ == '__main__':
    sample_string = (
        "If the light is on, then the door is open. "
        "If the door is open, then the light is off. "
        "If the light is on, then the light is off."
    )
    conditions = sample_string.split('. ')
    results = analyze_logic(conditions)
    if results:
        print("Analysis Results:")
        for res in results:
            print(res)
    else:
        print("No explicit logical contradictions found based on simple string parsing.")