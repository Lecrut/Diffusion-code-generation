import itertools
def check_equivalence(conditions1, conditions2):
    def evaluate(conditions):
        if not conditions:
            return True
        if len(conditions) != 2:
            raise ValueError("Each condition must have exactly two parts.")
        c1_a, c1_b = conditions[0]
        c2_a, c2_b = conditions[1]
        inputs = [True, False]
        for val1, val2 in itertools.product(inputs, repeat=2):
            result1 = (c1_a == val1) == (c1_b == val2)
            result2 = (c1_a == val2) == (c1_b == val1)
            if result1 != result2:
                return False
        return True
    def check_all_permutations(conditions):
        if len(conditions) != 2:
            return False
        c1_a, c1_b = conditions[0]
        c2_a, c2_b = conditions[1]
        inputs = [True, False]
        for val1, val2 in itertools.product(inputs, repeat=2):
            v1_perm1 = (c1_a == val1)
            v2_perm1 = (c1_b == val2)
            v1_perm2 = (c1_a == val2)
            v2_perm2 = (c1_b == val1)
            if not (v1_perm1 == v2_perm1 and v1_perm2 == v2_perm2):
                return False
        return True
    return check_all_permutations(conditions1) == check_all_permutations(conditions2)
if __name__ == '__main__':
    conditions1 = [('A', 'B'), ('A', 'B')]
    conditions2 = [('A', 'B'), ('A', 'B')]
    print(f"Example 1: {check_equivalence(conditions1, conditions2)}")
    conditions3 = [('A', 'B'), ('A', True)]
    conditions4 = [('A', 'B'), ('A', 'B')]
    print(f"Example 2: {check_equivalence(conditions3, conditions4)}")
    conditions5 = [('A', 'B'), ('B', 'A')]
    conditions6 = [('A', 'B'), ('A', 'B')]
    print(f"Example 3: {check_equivalence(conditions5, conditions6)}")
    conditions7 = [('A', 'B'), ('A', True)]
    conditions8 = [('A', 'B'), ('A', 'B')]
    print(f"Example 4: {check_equivalence(conditions7, conditions8)}")
    conditions9 = [('X', 'Y'), ('X', 'Y')]
    conditions10 = [('X', 'Y'), ('X', 'Y')]
    print(f"Example 5: {check_equivalence(conditions9, conditions10)}")
    conditions11 = [('X', 'Y'), ('X', 'Y')]
    conditions12 = [('Y', 'X'), ('Y', 'X')]
    print(f"Example 6: {check_equivalence(conditions11, conditions12)}")
    conditions13 = [('A', 'B'), ('A', True)]
    conditions14 = [('A', 'B'), ('A', 'B')]
    print(f"Example 7: {check_equivalence(conditions13, conditions14)}")