import itertools
def evaluate_expression(variables, expression):
    if not expression:
        return False
    sub_expressions = expression.split(' & ')
    if len(sub_expressions) == 1:
        if sub_expressions[0] == 'False':
            return False
        if sub_expressions[0] == 'True':
            return True
        if sub_expressions[0] == 'P':
            return variables.get('P', False)
        if sub_expressions[0] == 'Q':
            return variables.get('Q', False)
        if sub_expressions[0] == 'R':
            return variables.get('R', False)
        return False
    results = [evaluate_expression(variables, sub) for sub in sub_expressions]
    return all(results)
def check_contradiction(constraints):
    variables = {}
    for var in ['P', 'Q', 'R']:
        variables[var] = None
    all_combinations = list(itertools.product([True, False], repeat=3))
    for assignment in all_combinations:
        variables.update({
            'P': assignment[0],
            'Q': assignment[1],
            'R': assignment[2]
        })
        is_satisfied = True
        for constraint in constraints:
            if not evaluate_expression(variables, constraint):
                is_satisfied = False
                break
        if is_satisfied:
            return False
    return True
if __name__ == '__main__':
    constraints1 = [
        "P",
        "Q",
        "P & ~Q"
    ]
    print(f"Constraints 1: {constraints1}")
    print(f"Contradiction detected: {check_contradiction(constraints1)}")
    constraints2 = [
        "P",
        "~P"
    ]
    print(f"Constraints 2: {constraints2}")
    print(f"Contradiction detected: {check_contradiction(constraints2)}")
    constraints3 = [
        "P & Q",
        "Q & R",
        "R & P"
    ]
    print(f"Constraints 3: {constraints3}")
    print(f"Contradiction detected: {check_contradiction(constraints3)}")
    constraints4 = [
        "P",
        "Q"
    ]
    print(f"Constraints 4: {constraints4}")
    print(f"Contradiction detected: {check_contradiction(constraints4)}")