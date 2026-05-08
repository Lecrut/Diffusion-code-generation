def evaluate_logic(a, b, c):
    return (a and b) or (not c)
if __name__ == '__main__':
    print(evaluate_logic(True, True, False))
    print(evaluate_logic(True, False, True))
    print(evaluate_logic(False, False, False))
    print(evaluate_logic(True, True, True))