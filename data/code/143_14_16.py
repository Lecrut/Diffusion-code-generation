def detect_contradictions(constraints1, constraints2):
    false_outcomes1 = {constraint for constraint in constraints1 if not constraint}
    false_outcomes2 = {constraint for constraint in constraints2 if not constraint}
    return bool(false_outcomes1 & false_outcomes2)
if __name__ == '__main__':
    sample_constraints1 = [True, False, True]
    sample_constraints2 = [False, True, False]
    print(detect_contradictions(sample_constraints1, sample_constraints2))