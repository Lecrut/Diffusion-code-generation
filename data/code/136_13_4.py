def evaluate_logic(a: bool, b: bool, c: bool) -> bool:
    return a and (not b) or (c and a)
if __name__ == '__main__':
    print(evaluate_logic(True, False, True))
    print(evaluate_logic(False, True, False))