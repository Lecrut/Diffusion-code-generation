def detect_contradictions(constraints1, constraints2):
    false_outcomes1 = {constraint for constraint in constraints1 if not constraint()}
    false_outcomes2 = {constraint for constraint in constraints2 if not constraint()}
    return bool(false_outcomes1 & false_outcomes2)

if __name__ == '__main__':
    def constraint1():
        return False

    def constraint2():
        return True

    def constraint3():
        return False

    print(detect_contradictions([constraint1, constraint2], [constraint3]))