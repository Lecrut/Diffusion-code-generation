DECISION_A = 'Decision A'
DECISION_B = 'Decision B'
NO_DECISION = 'No Decision'

def evaluate_logic(a: bool, b: bool) -> str:
    if a and not b:
        return DECISION_A
    elif not a and b:
        return DECISION_B
    else:
        return NO_DECISION

if __name__ == '__main__':
    print(evaluate_logic(True, False))
    print(evaluate_logic(False, True))
    print(evaluate_logic(True, True))
    print(evaluate_logic(False, False))