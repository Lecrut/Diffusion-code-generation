def are_mutually_exclusive(constraints):
    if not constraints:
        return True
    all_constraints = set()
    for constraint_set in constraints:
        all_constraints.update(constraint_set)
    if len(all_constraints) == 0:
        return True
    for constraint_set in constraints:
        if not constraint_set.issubset(all_constraints):
            return False
    return True
if __name__ == '__main__':
    sample_constraints_1 = [
        {1, 2},
        {2, 3},
        {3, 1}
    ]
    print(f"Sample 1: {are_mutually_exclusive(sample_constraints_1)}")
    sample_constraints_2 = [
        {1, 2},
        {3, 4}
    ]
    print(f"Sample 2: {are_mutually_exclusive(sample_constraints_2)}")
    sample_constraints_3 = [
        {1, 2},
        {1, 3}
    ]
    print(f"Sample 3: {are_mutually_exclusive(sample_constraints_3)}")
    sample_constraints_4 = [
        {1, 2},
        {2, 1}
    ]
    print(f"Sample 4: {are_mutually_exclusive(sample_constraints_4)}")
    sample_constraints_5 = [
        {1, 2, 3},
        {1, 2}
    ]
    print(f"Sample 5: {are_mutually_exclusive(sample_constraints_5)}")