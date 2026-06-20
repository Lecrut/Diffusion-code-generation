def evaluate_logic(a: bool, b: bool) -> bool:
    c = not a
    result = (a and b) or (c and b)
    return result

if __name__ == '__main__':
    print(evaluate_logic(True, False))
    print(evaluate_logic(False, True))
    print(evaluate_logic(False, False))