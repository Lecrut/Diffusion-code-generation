def evaluate_expression(expression, assignment):
    if not expression:
        return False
    if expression == 'T':
        return True
    if expression == 'F':
        return False
    if expression == 'P':
        return assignment.get('P', False)
    if expression == 'Q':
        return assignment.get('Q', False)
    if expression == 'R':
        return assignment.get('R', False)
    return False
def check_contradiction(constraints):
    variables = {'P', 'Q', 'R'}
    all_assignments = []
    for p_val in [True, False]:
        for q_val in [True, False]:
            for r_val in [True, False]:
                assignment = {'P': p_val, 'Q': q_val, 'R': r_val}
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
    constraints1 = ['P', 'Q']
    print(f"Constraints: {constraints1}")
    print(f"Contradiction detected: {check_contradiction(constraints1)}")
    constraints2 = ['P', 'NOT P']
    print(f"Constraints: {constraints2}")
    print(f"Contradiction detected: {check_contradiction(constraints2)}")
    constraints3 = ['P', 'Q', 'NOT (P AND Q)']
    print(f"Constraints: {constraints3}")
    print(f"Contradiction detected: {check_contradiction(constraints3)}")
    constraints4 = ['P', 'Q', 'R']
    print(f"Constraints: {constraints4}")
    print(f"Contradiction detected: {check_contradiction(constraints4)}")