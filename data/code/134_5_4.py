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
    constraints1 = [
        {1, 2},
        {2, 3},
        {3, 4}
    ]
    print(f"Constraints 1 mutually exclusive: {are_mutually_exclusive(constraints1)}")
    constraints2 = [
        {1, 2},
        {2, 3},
        {1, 3}
    ]
    print(f"Constraints 2 mutually exclusive: {are_mutually_exclusive(constraints2)}")
    constraints3 = [
        {1, 2},
        {3, 4},
        {5, 6}
    ]
    print(f"Constraints 3 mutually exclusive: {are_mutually_exclusive(constraints3)}")
    constraints4 = [
        {1, 2, 3},
        {2, 3, 4}
    ]
    print(f"Constraints 4 mutually exclusive: {are_mutually_exclusive(constraints4)}")
    constraints5 = [
        {1, 2},
        {2, 1}
    ]
    print(f"Constraints 5 mutually exclusive: {are_mutually_exclusive(constraints5)}")