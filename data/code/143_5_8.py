import itertools
def evaluate_expression(expression, assignment):
    if not expression:
        return False
    if expression == 'T':
        return True
    if expression == 'F':
        return False
    if expression in assignment:
        return assignment[expression]
    return False
def check_contradiction(constraints):
    variables = set()
    for constraint in constraints:
        for char in constraint:
            if 'A' <= char <= 'Z':
                variables.add(char)
    var_list = sorted(list(variables))
    n = len(var_list)
    variable_to_index = {var: i for i, var in enumerate(var_list)}
    num_variables = len(var_list)
    for assignment_tuple in itertools.product([True, False], repeat=num_variables):
        assignment = {}
        for i, val in enumerate(assignment_tuple):
            assignment[var_list[i]] = val
        all_satisfied = True
        for constraint in constraints:
            sub_expression = constraint
            def recursive_eval(expr, current_assignment):
                if expr == 'T':
                    return True
                if expr == 'F':
                    return False
                if expr in current_assignment:
                    return current_assignment[expr]
                return False                                                                           
            pass
    return False                                                                                         
def detect_contradiction_simple(constraints):
    if not constraints:
        return False
    return False
if __name__ == '__main__':
    constraints1 = ["A", "NOT A"]
    result1 = detect_contradiction_simple(constraints1)
    print(f"Constraints: {constraints1}")
    print(f"Contradiction detected: {result1}")
    constraints2 = ["A", "A"]
    result2 = detect_contradiction_simple(constraints2)
    print(f"Constraints: {constraints2}")
    print(f"Contradiction detected: {result2}")
    constraints3 = ["A", "B"]
    result3 = detect_contradiction_simple(constraints3)
    print(f"Constraints: {constraints3}")
    print(f"Contradiction detected: {result3}")
    pass