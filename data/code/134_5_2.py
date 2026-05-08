def are_mutually_exclusive(constraints):
    if not constraints:
        return True
    all_sets = [set(s) for s in constraints]
    for i in range(len(all_sets)):
        for j in range(i + 1, len(all_sets)):
            if not all_sets[i].isdisjoint(all_sets[j]):
                return False
    return True
if __name__ == '__main__':
    sample_constraints_1 = [
        {'a', 'b'},
        {'b', 'c'},
        {'c', 'a'}
    ]
    print(f"Sample 1: {are_mutually_exclusive(sample_constraints_1)}")
    sample_constraints_2 = [
        {'a', 'b'},
        {'c', 'd'},
        {'e', 'f'}
    ]
    print(f"Sample 2: {are_mutually_exclusive(sample_constraints_2)}")
    sample_constraints_3 = [
        {'a', 'b'},
        {'b', 'c'},
        {'a', 'c'}
    ]
    print(f"Sample 3: {are_mutually_exclusive(sample_constraints_3)}")
    sample_constraints_4 = [
        {'a', 'b'},
        {'b', 'a'}
    ]
    print(f"Sample 4: {are_mutually_exclusive(sample_constraints_4)}")
    sample_constraints_5 = [
        {'x', 'y', 'z'},
        {'y', 'z', 'w'},
        {'z', 'w', 'x'}
    ]
    print(f"Sample 5: {are_mutually_exclusive(sample_constraints_5)}")