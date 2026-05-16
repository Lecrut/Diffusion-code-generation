class ExclusivityChecker:
    def are_mutually_exclusive(self, sets: list[set]) -> bool:
        seen_elements = set()
        for s in sets:
            if not seen_elements.isdisjoint(s):
                return False
            seen_elements.update(s)
        return True
if __name__ == '__main__':
    checker = ExclusivityChecker()
    sets1 = [
        {1, 2},
        {3, 4},
        {5, 6}
    ]
    print(f"Test Case 1: {checker.are_mutually_exclusive(sets1)}")
    sets2 = [
        {1, 2},
        {2, 3},
        {4, 5}
    ]
    print(f"Test Case 2: {checker.are_mutually_exclusive(sets2)}")
    sets3 = [
        {1, 2},
        {3, 4},
        {2, 4}
    ]
    print(f"Test Case 3: {checker.are_mutually_exclusive(sets3)}")
    sets4 = []
    print(f"Test Case 4: {checker.are_mutually_exclusive(sets4)}")
    sets5 = [
        {10, 20},
        {20, 30},
        {40, 50}
    ]
    print(f"Test Case 5: {checker.are_mutually_exclusive(sets5)}")
    sets6 = [
        {1, 2},
        {1, 2}
    ]
    print(f"Test Case 6: {checker.are_mutually_exclusive(sets6)}")