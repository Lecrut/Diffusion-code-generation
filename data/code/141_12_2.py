def evaluate_logic(A: bool, B: bool, C: bool) -> bool:
    result = (A and B) or (not C)
    return result
if __name__ == '__main__':
    print(evaluate_logic(True, True, False))
    print(evaluate_logic(True, False, True))
    print(evaluate_logic(False, True, False))
    print(evaluate_logic(False, False, True))