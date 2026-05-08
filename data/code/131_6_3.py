import os
def simulate_decision_making(rules_file, input_variable):
    results = []
    try:
        with open(rules_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                try:
                    rule_line = line.split(':')
                    if len(rule_line) == 2:
                        rule_condition = rule_line[0].strip()
                        rule_output = rule_line[1].strip()
                        if rule_condition == input_variable:
                            results.append(rule_output)
                        else:
                            results.append(f"No rule found for {input_variable}")
                    else:
                        results.append(f"Malformed rule line: {line}")
                except Exception as e:
                    results.append(f"Error processing line: {line} - {e}")
    except FileNotFoundError:
        return [f"Error: Rules file '{rules_file}' not found."]
    return results
if __name__ == '__main__':
    RULES_FILE = "rules.txt"
    INPUT_VALUE = "A"
    with open(RULES_FILE, 'w') as f:
        f.write("# Rule: If input is A, output is True\n")
        f.write("A:True\n")
        f.write("B:False\n")
        f.write("C:True\n")
        f.write("D:False\n")
    simulation_results = simulate_decision_making(RULES_FILE, INPUT_VALUE)
    for result in simulation_results:
        print(result)