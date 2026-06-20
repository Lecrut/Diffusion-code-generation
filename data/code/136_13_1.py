def evaluate_logic(a: bool, b: bool) -> str:
    if a and (not b):
        return 'Decision A'
    elif not a and b:
        return 'Decision B'
    else:
        return 'No Decision'
if __name__ == '__main__':
    print(evaluate_logic(True, False))
    print(evaluate_logic(False, True))
    print(evaluate_logic(True, True))
    print(evaluate_logic(False, False))