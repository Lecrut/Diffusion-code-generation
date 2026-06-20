def evaluate_boolean_expression(expression: str) -> bool:
    return eval(expression)

if __name__ == '__main__':
    print(evaluate_boolean_expression("True"))
    print(evaluate_boolean_expression("False"))
    print(evaluate_boolean_expression("1 == 1"))
    print(evaluate_boolean_expression("2 > 3"))