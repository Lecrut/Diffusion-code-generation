import re
def analyze_logic(conditions):
    parsed_conditions = []
    for cond in conditions:
        match = re.match(r"^\s*if\s+(.*)\s*:\s*(.*)$", cond.strip())
        if match:
            condition_str = match.group(1).strip()
            result_str = match.group(2).strip()
            parsed_conditions.append((condition_str, result_str))
        else:
            parsed_conditions.append((cond, "ERROR_PARSE"))
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
                contradictions.append(f"Contradiction found between condition '{cond1}': Result 1 is '{res1}', Result 2 is '{res2}'")
    return contradictions
if __name__ == '__main__':
    sample_string = (
        "if temperature > 30: result is hot\n"
        "if temperature > 30: result is cold\n"
        "if light_on: action is turn_on\n"
        "if light_on: action is turn_off\n"
        "if age >= 18: status is adult\n"
        "if age >= 18: status is minor"
    )
    parsed = analyze_logic(sample_string.split('\n'))
    results = check_contradictions(parsed)
    if results:
        print("Logical Contradictions Found:")
        for res in results:
            print(res)
    else:
        print("No explicit logical contradictions found based on identical conditions.")