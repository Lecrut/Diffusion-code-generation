MAX_VARIABLES = 10

def detect_contradictions(statements):
    variables = set()
    truth_assignments = [None] * MAX_VARIABLES
    for statement in statements:
        if not isinstance(statement, tuple) or len(statement) != 3:
            continue
        condition, value, variable_index = statement
        var_name = f'var{variable_index}'
        if var_name not in variables:
            variables.add(var_name)
            truth_assignments[variable_index] = None
        if condition:
            current_value = truth_assignments[variable_index]
            if current_value is not None and current_value != value:
                return True
    return False
if __name__ == '__main__':
    statements1 = [('x > 5', 6, 0), ('x < 3', 2, 0)]
    statements2 = [('y > 10', 15, 1), ('y < 5', 4, 1)]
    print(detect_contradictions(statements1))
    print(detect_contradictions(statements2))