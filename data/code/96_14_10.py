def evaluate_expression(a: bool, b: bool) -> bool:
    c = not a or b
    return a and b or (not a and c)
if __name__ == '__main__':
    print(evaluate_expression(True, False))
    print(evaluate_expression(False, True))
    print(evaluate_expression(False, False))