class ExclusivityChecker:
    def are_mutually_exclusive(self, sets):
        n = len(sets)
        for i in range(n):
            for j in range(i + 1, n):
                if not sets[i].isdisjoint(sets[j]):
                    return False
        return True
if __name__ == '__main__':
    checker = ExclusivityChecker()
    sets1 = [
        {1, 2},
        {3, 4},
        {5, 6}
    ]
    print(f"Sets 1: {sets1}, Exclusive: {checker.are_mutually_exclusive(sets1)}")
    sets2 = [
        {1, 2, 3},
        {3, 4},
        {5, 6}
    ]
    print(f"Sets 2: {sets2}, Exclusive: {checker.are_mutually_exclusive(sets2)}")
    sets3 = [
        {1, 2},
        {3, 4},
        {1, 5}
    ]
    print(f"Sets 3: {sets3}, Exclusive: {checker.are_mutually_exclusive(sets3)}")
    sets4 = [
        {1},
        set(),
        {2}
    ]
    print(f"Sets 4: {sets4}, Exclusive: {checker.are_mutually_exclusive(sets4)}")
    sets5 = [
        {1, 2},
        {1, 2}
    ]
    print(f"Sets 5: {sets5}, Exclusive: {checker.are_mutually_exclusive(sets5)}")
    sets6 = [
        {1, 2, 3},
        {3, 4, 5},
        {6, 7}
    ]
    print(f"Sets 6: {sets6}, Exclusive: {checker.are_mutually_exclusive(sets6)}")