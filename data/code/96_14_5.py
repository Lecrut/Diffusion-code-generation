def evaluate_logic(a: bool, b: bool) -> bool:
    c = a ^ b
    return a & b | ~a & c
if __name__ == '__main__':
    print(evaluate_logic(True, False))
    print(evaluate_logic(False, True))
    print(evaluate_logic(True, True))
    print(evaluate_logic(False, False))