def are_mutually_exclusive(constraints):
    if not constraints:
        return True
    all_constraints = set()
    for constraint_set in constraints:
        all_constraints.update(constraint_set)
    for i in range(len(constraints)):
        current_constraint = constraints[i]
        if not current_constraint.issubset(all_constraints):
            return False
    return True
if __name__ == '__main__':
    sample_constraints = [
        {1, 2},
        {2, 3},
        {3, 1}
    ]
    print(are_mutually_exclusive(sample_constraints))
    sample_constraints_2 = [
        {1, 2},
        {3, 4}
    ]
    print(are_mutually_exclusive(sample_constraints_2))
    sample_constraints_3 = [
        {1, 2},
        {1, 2, 3}
    ]
    print(are_mutually_exclusive(sample_constraints_3))
    sample_constraints_4 = [
        {1, 2},
        {2, 1}
    ]
    print(are_mutually_exclusive(sample_constraints_4))