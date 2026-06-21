def detect_contradictions(constraints1, constraints2):
    false_outcomes1 = set()
    for constraint in constraints1:
        if not constraint():
            false_outcomes1.add(id(constraint))

    false_outcomes2 = set()
    for constraint in constraints2:
        if not constraint():
            false_outcomes2.add(id(constraint))

    return bool(false_outcomes1 & false_outcomes2)

if __name__ == '__main__':
    def constraint1():
        return False

    def constraint2():
        return True

    def constraint3():
        return False

    constraints_set1 = [constraint1, constraint2]
    constraints_set2 = [constraint3]

    print(detect_contradictions(constraints_set1, constraints_set2))