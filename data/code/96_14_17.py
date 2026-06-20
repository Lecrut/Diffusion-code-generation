def evaluate_logic(a: bool, b: bool) -> bool:
    c = a ^ b
    return a & b | ~a & c
if __name__ == '__main__':
    print(evaluate_logic(True, False))