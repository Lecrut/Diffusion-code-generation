import os
def simulate_decision_making(rules_file, input_variable):
    results = []
    try:
        with open(rules_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split(':')
                if len(parts) == 2:
                    rule_key = parts[0].strip()
                    rule_value = parts[1].strip()
                    if rule_key == input_variable:
                        results.append(rule_value)
                    else:
                        results.append(f"No rule found for {input_variable}")
                else:
                    results.append(f"Malformed line: {line}")
    except FileNotFoundError:
        return [f"Error: Rules file {rules_file} not found"]
    return results
if __name__ == '__main__':
    RULES_FILE = "rules.txt"
    INPUT = "temperature"
    with open(RULES_FILE, 'w') as f:
        f.write("# Rule: temperature decisions\n")
        f.write("temperature:hot\n")
        f.write("temperature:cold\n")
        f.write("humidity:high\n")
        f.write("humidity:low\n")
    output = simulate_decision_making(RULES_FILE, INPUT)
    for result in output:
        print(result)