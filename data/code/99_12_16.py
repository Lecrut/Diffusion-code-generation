def evaluate_conditions(a, b, c):
    return a and (b or not c)
if __name__ == '__main__':
    print(evaluate_conditions(True, False, True))
    print(evaluate_conditions(True, True, False))
    print(evaluate_conditions(False, False, False))