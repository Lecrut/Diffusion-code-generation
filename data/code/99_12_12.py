def evaluate_conditions(a, b, c):
    return a or (b and c)
if __name__ == '__main__':
    print(evaluate_conditions(True, False, True))
    print(evaluate_conditions(False, True, False))
    print(evaluate_conditions(False, False, True))
    print(evaluate_conditions(True, True, True))