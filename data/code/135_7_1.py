import itertools
def check_equivalence(conditions1, conditions2):
    def evaluate(conditions):
        if not conditions:
            return True
        if len(conditions) != 2:
            raise ValueError("Each condition must have exactly two parts.")
        c1_a, c1_b = conditions[0]
        c2_a, c2_b = conditions[1]
        val1 = (c1_a and c1_b)
        val2 = (c2_a and c2_b)
        return val1 == val2
    all_permutations1 = list(itertools.permutations(conditions1))
    all_permutations2 = list(itertools.permutations(conditions2))
    for p1 in all_permutations1:
        for p2 in all_permutations2:
            if not evaluate((p1, p2)):
                return False
    return True
if __name__ == '__main__':
    conditions_a = [
        (True, True),
        (False, False)
    ]
    conditions_b = [
        (True, True),
        (False, False)
    ]
    conditions_c = [
        (True, False),
        (False, True)
    ]
    print(f"Test 1 (A vs B): {check_equivalence(conditions_a, conditions_b)}")
    print(f"Test 2 (A vs C): {check_equivalence(conditions_a, conditions_c)}")
    print(f"Test 3 (B vs C): {check_equivalence(conditions_b, conditions_c)}")