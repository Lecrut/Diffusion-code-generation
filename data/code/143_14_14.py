def detect_contradictions(constraints1, constraints2):
    false_outcomes1 = {c for c in constraints1 if not constraints1[c]}
    false_outcomes2 = {c for c in constraints2 if not constraints2[c]}
    return bool(false_outcomes1 & false_outcomes2)

if __name__ == '__main__':
    constraints1 = {'A': True, 'B': False, 'C': True}
    constraints2 = {'A': False, 'B': True, 'D': False}
    print(detect_contradictions(constraints1, constraints2))