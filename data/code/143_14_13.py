def detect_contradictions(constraints1, constraints2):
    false_outcomes1 = set()
    false_outcomes2 = set()

    for constraint in constraints1:
        if not constraint():
            false_outcomes1.add(frozenset(constraint.__code__.co_varnames))

    for constraint in constraints2:
        if not constraint():
            false_outcomes2.add(frozenset(constraint.__code__.co_varnames))

    return bool(false_outcomes1 & false_outcomes2)

if __name__ == '__main__':
    def constraint1(x, y):
        return x > 0 and y < 0

    def constraint2(y, z):
        return y < 0 and z >= 0

    print(detect_contradictions([constraint1], [constraint2]))