import itertools
def check_equivalence(conditions1, conditions2):
    def evaluate(conditions):
        if not conditions:
            return True
        if len(conditions) == 1:
            op, val1, val2 = conditions[0]
            if op == '==':
                return val1 == val2
            elif op == '!=':
                return val1 != val2
            elif op == '>':
                return val1 > val2
            elif op == '<':
                return val1 < val2
            elif op == '>=':
                return val1 >= val2
            elif op == '<=':
                return val1 <= val2
            return False
        if len(conditions) == 2:
            op, val1, val2 = conditions[0]
            if op == '==':
                return val1 == val2
            elif op == '!=':
                return val1 != val2
            elif op == '>':
                return val1 > val2
            elif op == '<':
                return val1 < val2
            elif op == '>=':
                return val1 >= val2
            elif op == '<=':
                return val1 <= val2
            return False
        if len(conditions) == 3:
            op1, val1, val2 = conditions[0]
            if op1 == '==':
                if val1 == val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 != val2:
                    return conditions[1][0] == conditions[1][1]
            elif op1 == '!=':
                if val1 != val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 == val2:
                    return conditions[1][0] == conditions[1][1]
            elif op1 == '>':
                if val1 > val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 < val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 == val2:
                    return conditions[1][0] == conditions[1][1]
            elif op1 == '<':
                if val1 < val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 > val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 == val2:
                    return conditions[1][0] == conditions[1][1]
            elif op1 == '>=':
                if val1 >= val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 < val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 == val2:
                    return conditions[1][0] == conditions[1][1]
            elif op1 == '<=':
                if val1 <= val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 > val2:
                    return conditions[1][0] == conditions[1][1]
                elif val1 == val2:
                    return conditions[1][0] == conditions[1][1]
            return False
        return False
    def check_all_permutations(conds1, conds2):
        if len(conds1) != len(conds2):
            return False
        for p1 in itertools.permutations(conds1):
            p2 = list(itertools.permutations(conds2))
            for p1_tuple, p2_tuple in itertools.permutations(p1):
                if evaluate(p1_tuple) != evaluate(p2_tuple):
                    return False
        return True
    if len(conditions1) != len(conditions2):
        return False
    all_conds1 = list(itertools.permutations(conditions1))
    all_conds2 = list(itertools.permutations(conditions2))
    for p1 in all_conds1:
        for p2 in all_conds2:
            if evaluate(p1) != evaluate(p2):
                return False
    return True
if __name__ == '__main__':
    conditions_a = [('==', True, False), ('<', 10, 20)]
    conditions_b = [('==', True, False), ('<', 10, 20)]
    conditions_c = [('==', False, True), ('<', 10, 20)]
    print(f"A and B equivalent: {check_equivalence(conditions_a, conditions_b)}")
    print(f"A and C equivalent: {check_equivalence(conditions_a, conditions_c)}")
    conditions_d = [('==', True, False), ('<', 5, 10)]
    conditions_e = [('==', True, False), ('<', 5, 10)]
    conditions_f = [('==', False, True), ('<', 5, 10)]
    print(f"D and E equivalent: {check_equivalence(conditions_d, conditions_e)}")
    print(f"D and F equivalent: {check_equivalence(conditions_d, conditions_f)}")
    conditions_g = [('==', True, False)]
    conditions_h = [('==', False, True)]
    print(f"G and H equivalent: {check_equivalence(conditions_g, conditions_h)}")