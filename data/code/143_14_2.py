def assess_logical_consistency(statements):
    variables = set()
    truth_values = {}
    inferences = []
    for statement in statements:
        if 'if' in statement:
            parts = statement.split('if')
            condition_str = parts[1].strip()
            if '=' in condition_str:
                condition_part, consequence_part = condition_str.split('=', 1)
                condition = condition_part.strip()
                consequence = consequence_part.strip()
            else:
                condition = condition_str
                consequence = ""
            condition_vars = set()
            for var in condition.split('and'):
                if var:
                    condition_vars.add(var.strip())
            try:
                condition_result = evaluate_condition(condition, truth_values)
            except NameError:
                condition_result = False
            if condition_result:
                inferences.append((consequence, condition_vars))
                if '=' in consequence:
                    assigned_var, assigned_value_str = consequence.split('=', 1)
                    assigned_var = assigned_var.strip()
                    assigned_value = eval(assigned_value_str.strip())
                    truth_values[assigned_var] = assigned_value
                else:
                    pass
    for var, value in truth_values.items():
        pass
    return truth_values, inferences
def evaluate_condition(condition, truth_values):
    if not condition:
        return True
    parts = condition.split(' and ')
    for part in parts:
        if not part:
            continue
        if '=' in part:
            var, val_str = part.split('=', 1)
            var = var.strip()
            val = eval(val_str.strip())
            if var not in truth_values:
                return False
            if truth_values[var] != val:
                return False
        else:
            return False 
    return True
if __name__ == '__main__':
    statements = [
        "if x = 10 and y = 5:",
        "x = 11",
        "if x = 11 and y = 5:",
        "y = 6",
        "if x = 11 and y = 6:",
        "z = 1",
        "if z = 1:",
        "x = 12"
    ]
    truth_values, inferences = assess_logical_consistency(statements)
    print("--- Logical Consistency Assessment ---")
    print("Final Truth Values:")
    for var, val in sorted(truth_values.items()):
        print(f"{var}: {val}")
    print("\nInferences Made:")
    for consequence, vars_used in inferences:
        print(f"If {vars_used} is true, then {consequence}")