import itertools
def are_mutually_exclusive(constraints):
    if not constraints:
        return True
    sets = list(constraints)
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if not sets[i].isdisjoint(sets[j]):
                return False
    return True
if __name__ == '__main__':
    sample_constraints = [
        {'a', 'b'},
        {'b', 'c'},
        {'c', 'd'},
        {'d', 'a'}
    ]
    sample_constraints_2 = [
        {'a', 'b'},
        {'c', 'd'},
        {'a', 'c'}
    ]
    sample_constraints_3 = [
        {'a', 'b'},
        {'b', 'c'},
        {'c', 'a'}
    ]
    print(f"Sample 1 mutually exclusive: {are_mutually_exclusive(sample_constraints)}")
    print(f"Sample 2 mutually exclusive: {are_mutually_exclusive(sample_constraints_2)}")
    print(f"Sample 3 mutually exclusive: {are_mutually_exclusive(sample_constraints_3)}")