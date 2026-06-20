def evaluate_logic(a: bool, b: bool) -> bool:
    c = a or not b
    return (a and b) or (not a and c)

if __name__ == '__main__':
    print(evaluate_logic(True, False))
    print(evaluate_logic(False, True))
    print(evaluate_logic(True, True))
    print(evaluate_logic(False, False))