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
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                assignment = {'A': a, 'B': b, 'C': c}
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
    print(f"Contradiction detected: {check_contradiction(constraints1)}")
    constraints2 = ['A', 'B', 'C']
    print(f"Constraints: {constraints2}")
    print(f"Contradiction detected: {check_contradiction(constraints2)}")
    constraints3 = ['A', 'B', 'C', 'not (A and B)', 'not (B and C)']
    print(f"Constraints: {constraints3}")
    print(f"Contradiction detected: {check_contradiction(constraints3)}")
    constraints4 = ['A', 'not A']
    print(f"Constraints: {constraints4}")
    print(f"Contradiction detected: {check_contradiction(constraints4)}")
    constraints5 = ['A', 'B', 'C']
    print(f"Constraints: {constraints5}")
    print(f"Contradiction detected: {check_contradiction(constraints5)}")