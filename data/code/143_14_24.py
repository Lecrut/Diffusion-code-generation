def detect_contradictions(constraints1, constraints2):
    false_outcomes1 = {constraint for constraint in constraints1 if not eval(constraint)}
    false_outcomes2 = {constraint for constraint in constraints2 if not eval(constraint)}
    return bool(false_outcomes1 & false_outcomes2)

if __name__ == '__main__':
    constraints_set1 = ["x > 5", "y < 3"]
    constraints_set2 = ["x <= 5", "z == 7"]
    print(detect_contradictions(constraints_set1, constraints_set2))