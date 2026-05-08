import itertools
def evaluate_conditions(conditions, variables):
    results = {}
    for condition, var_name in conditions:
        if var_name in variables:
            result = eval(condition, {"__builtins__": None}, variables)
            results[var_name] = result
        else:
            results[var_name] = "Undefined"
    return results
def check_consistency(conditions, initial_values):
    all_conditions = []
    for condition, var_name in conditions:
        all_conditions.append((condition, var_name))
    inconsistent_sets = set()
    for values in itertools.product(*(range(min(10, 5)) for _ in range(len(initial_values)))) if initial_values else [()] :
        current_values = {}
        consistent = True
        for condition, var_name in all_conditions:
            try:
                result = eval(condition, {"__builtins__": None}, current_values)
                if var_name in current_values:
                    if current_values[var_name] != result:
                        consistent = False
                        break
                    current_values[var_name] = result
                else:
                    current_values[var_name] = result
            except NameError:
                consistent = False
                break
            except Exception:
                consistent = False
                break
        if consistent:
            inconsistent_sets.add(tuple(sorted(current_values.items())))
    return inconsistent_sets
if __name__ == '__main__':
    conditions = [
        ("x > 5 and y < 10", "x"),
        ("x == 6", "x"),
        ("y == 5", "y"),
        ("x + y == 11", "x"),
        ("x == 7", "x")
    ]
    initial_values = [6, 5]
    inconsistencies = check_consistency(conditions, initial_values)
    print(f"Conditions: {conditions}")
    print(f"Initial Values: {initial_values}")
    print(f"Inconsistent States Found: {inconsistencies}")