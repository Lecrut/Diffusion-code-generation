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
    constraints1 = [
        {1, 2},
        {2, 3},
        {3, 1}
    ]
    print(f"Constraints 1 mutually exclusive: {are_mutually_exclusive(constraints1)}")
    constraints2 = [
        {1, 2},
        {3, 4}
    ]
    print(f"Constraints 2 mutually exclusive: {are_mutually_exclusive(constraints2)}")
    constraints3 = [
        {1, 2},
        {1, 3}
    ]
    print(f"Constraints 3 mutually exclusive: {are_mutually_exclusive(constraints3)}")
    constraints4 = [
        {1, 2, 3},
        {1, 2}
    ]
    print(f"Constraints 4 mutually exclusive: {are_mutually_exclusive(constraints4)}")
    constraints5 = [
        {1, 2},
        {3, 4},
        {1, 3}
    ]
    print(f"Constraints 5 mutually exclusive: {are_mutually_exclusive(constraints5)}")