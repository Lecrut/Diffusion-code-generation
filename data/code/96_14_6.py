def evaluate_nested_boolean_expression(a: bool, b: bool) -> bool:
    c = a or not b
    return a and b or (not a and c)
if __name__ == '__main__':
    print(evaluate_nested_boolean_expression(True, False))
    print(evaluate_nested_boolean_expression(False, True))
    print(evaluate_nested_boolean_expression(True, True))
    print(evaluate_nested_boolean_expression(False, False))