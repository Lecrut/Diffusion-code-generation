import itertools
def are_mutually_exclusive(constraints):
    if not constraints:
        return True
    n = len(constraints)
    for i in range(n):
        for j in range(i + 1, n):
            if not constraints[i].isdisjoint(constraints[j]):
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
        {3, 4}
    ]
    print(f"Constraints 3 mutually exclusive: {are_mutually_exclusive(constraints3)}")
    constraints4 = [
        {1, 2, 3},
        {2, 3, 4}
    ]
    print(f"Constraints 4 mutually exclusive: {are_mutually_exclusive(constraints4)}")
    constraints5 = [
        {1, 2},
        {1, 2}
    ]
    print(f"Constraints 5 mutually exclusive: {are_mutually_exclusive(constraints5)}")
    constraints6 = [
        {1, 2},
        {1, 2, 3}
    ]
    print(f"Constraints 6 mutually exclusive: {are_mutually_exclusive(constraints6)}")