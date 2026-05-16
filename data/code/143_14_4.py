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
                pass
            pass
    defined_variables = set()
    assignments = {}
    for stmt in statements:
        if 'if' in stmt:
            try:
                condition_part, rest = stmt.split('if', 1)
                condition = condition_part.strip()
                if '=' in rest:
                    condition_part, assignment_part = rest.split('=', 1)
                    condition = condition_part.strip()
                    value = assignment_part.strip()
                    if ' ' in value:
                        var, val = value.split(' ', 1)
                        assignments[var] = val
                        defined_variables.add(var)
                    else:
                        assignments[condition.split(' ')[0]] = True                                          
                        defined_variables.add(condition.split(' ')[0])
            except ValueError:
                continue
    for var, val in assignments.items():
        if var in assignments and assignments[var] != val:
            return False, f"Contradiction found for variable {var}: assigned {assignments[var]} and {val}"
    return True, "No logical contradictions found based on explicit assignments."
if __name__ == '__main__':
    statements1 = [
        "if x > 5: x = 10",
        "if y < 10: y = 20"
    ]
    result1, message1 = assess_logical_consistency(statements1)
    print(f"--- Test Case 1 ---")
    print(f"Consistent: {result1}")
    print(f"Message: {message1}\n")
    statements2 = [
        "if a > 0: a = 5",
        "if a < 0: a = -5"                                                                                                              
    ]
    result2, message2 = assess_logical_consistency(statements2)
    print(f"--- Test Case 2 ---")
    print(f"Consistent: {result2}")
    print(f"Message: {message2}\n")
    statements3 = [
        "if x == x: True"
    ]
    result3, message3 = assess_logical_consistency(statements3)
    print(f"--- Test Case 3 ---")
    print(f"Consistent: {result3}")
    print(f"Message: {message3}\n")