def assess_logical_consistency(statements):
    variables = set()
    truth_assignments = {}
    inconsistencies = []
    for statement in statements:
        if not isinstance(statement, tuple) or len(statement) != 3:
            inconsistencies.append(f"Invalid statement format: {statement}")
            continue
        condition, value, variable = statement
        if variable not in variables:
            variables.add(variable)
            truth_assignments[variable] = None
        if condition:
            if variable in truth_assignments and truth_assignments[variable] is not None and truth_assignments[variable] != value:
                inconsistencies.append(f"Contradiction found for variable {variable}: Condition {condition} implies {variable} is {value}, but previous assignment was {truth_assignments[variable]}")
            else:
                truth_assignments[variable] = value
        else:
            if variable in truth_assignments and truth_assignments[variable] is not None and truth_assignments[variable] != value:
                inconsistencies.append(f"Contradiction found for variable {variable}: Condition {condition} implies {variable} is not {value}, but previous assignment was {truth_assignments[variable]}")
            else:
                truth_assignments[variable] = value
    return inconsistencies, truth_assignments
if __name__ == '__main__':
    sample_statements = [
        (True, 10, 'A'),
        (False, 5, 'A'),
        (True, 10, 'B'),
        (False, 20, 'B'),
        (True, 10, 'A')
    ]
    inconsistencies, assignments = assess_logical_consistency(sample_statements)
    print("--- Logical Consistency Assessment ---")
    if inconsistencies:
        print("Inconsistencies Found:")
        for inc in inconsistencies:
            print(inc)
    else:
        print("No logical inconsistencies found.")
    print("\nFinal Assignments:")
    for var, val in sorted(assignments.items()):
        print(f"{var}: {val}")