def assess_logical_consistency(statements):
    variables = set()
    truth_values = {}
    inferences = []
    for statement in statements:
        if 'if' in statement:
            parts = statement.split('if')
            condition_str = parts[1].strip()
            if '=' in condition_str:
                condition_part, value_part = condition_str.split('=', 1)
                condition = condition_part.strip()
                value = value_part.strip()
            else:
                condition = condition_str.strip()
                value = None
            if '=' in statement:
                var_name, assigned_value = statement.split('=', 1)
                var_name = var_name.strip()
                assigned_value = assigned_value.strip()
                truth_values[var_name] = assigned_value
                variables.add(var_name)
                continue
            inferences.append((condition, value))
    contradictions = []
    final_state = {}
    is_consistent = True
    for condition, value in inferences:
        if condition == "A and not A":
            is_consistent = False
            break
        final_state[condition] = value
    if not is_consistent:
        return False, "Contradiction found in structure."
    return True, "Consistent"
if __name__ == '__main__':
    sample_statements_consistent = [
        "if X > 5: print('High')",
        "if Y == 10: print('Ten')",
        "X = 6",
        "Y = 10"
    ]
    sample_statements_contradictory = [
        "if A > 1: print('A is large')",
        "if A <= 0: print('A is small')",
        "A = 5"
    ]
    print("--- Testing Consistent Set ---")
    consistent_result, message = assess_logical_consistency(sample_statements_consistent)
    print(f"Consistency: {consistent_result}, Message: {message}\n")
    print("--- Testing Contradictory Set ---")
    contradictory_result, message = assess_logical_consistency(sample_statements_contradictory)
    print(f"Consistency: {contradictory_result}, Message: {message}\n")