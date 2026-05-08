import itertools
def check_equivalence(conditions1, conditions2):
    def evaluate(conditions):
        if not conditions:
            return True
        if len(conditions) != 2:
            raise ValueError("Each condition must have exactly two parts.")
        result1 = conditions[0][0]
        result2 = conditions[1][0]
        if len(conditions) == 1:
            return result1
        if len(conditions) == 2:
            return result1 == result2
        return None
    def check_all_permutations(conditions):
        if not conditions:
            return True
        results = set()
        for p in itertools.permutations(conditions):
            try:
                result = evaluate(list(p))
                if result is not None:
                    results.add(result)
            except ValueError:
                continue
        return results
    results1 = check_all_permutations(conditions1)
    results2 = check_all_permutations(conditions2)
    return results1 == results2
if __name__ == '__main__':
    conditions_a = [
        [True, True],
        [False, False]
    ]
    conditions_b = [
        [True, False],
        [False, True]
    ]
    print(check_equivalence(conditions_a, conditions_b))
    conditions_c = [
        [True, True],
        [True, True]
    ]
    conditions_d = [
        [True, True],
        [True, True]
    ]
    print(check_equivalence(conditions_c, conditions_d))
    conditions_e = [
        [True, True],
        [False, False]
    ]
    conditions_f = [
        [False, False],
        [True, True]
    ]
    print(check_equivalence(conditions_e, conditions_f))