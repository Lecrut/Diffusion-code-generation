def evaluate_expression(expression, assignment):
    if not expression:
        return False
    if expression == 'T':
        return True
    if expression == 'F':
        return False
    if expression == 'A':
        return assignment.get('A', False)
    if expression == 'B':
        return assignment.get('B', False)
    if expression == 'C':
        return assignment.get('C', False)
    return False
def check_contradiction(constraints):
    variables = {'A', 'B', 'C'}
    all_assignments = []
    for i in range(2**len(variables)):
        assignment = {}
        for var in variables:
            assignment[var] = 'T' if (i >> (len(variables) - 1 - list(variables).index(var))) % 2 else 'F'
        is_consistent = True
        for constraint in constraints:
            if not evaluate_expression(constraint, assignment):
                is_consistent = False
                break
        if is_consistent:
            all_assignments.append(assignment)
    if not all_assignments:
        return False
    return True
if __name__ == '__main__':
    constraints1 = ['A', 'B']
    print(f"Constraints: {constraints1}")
    result1 = check_contradiction(constraints1)
    print(f"Contradiction detected: {result1}")
    constraints2 = ['A', 'B', 'C']
    print(f"Constraints: {constraints2}")
    result2 = check_contradiction(constraints2)
    print(f"Contradiction detected: {result2}")
    constraints3 = ['A', 'B', 'C', 'NOT(A AND B)', 'NOT(C)']
    print(f"Constraints: {constraints3}")
    result3 = check_contradiction(constraints3)
    print(f"Contradiction detected: {result3}")
    constraints4 = ['A', 'NOT(A)']
    print(f"Constraints: {constraints4}")
    result4 = check_contradiction(constraints4)
    print(f"Contradiction detected: {result4}")