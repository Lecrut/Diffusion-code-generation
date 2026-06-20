def evaluate_boolean_expression(expression: str) -> bool:
    return eval(compile(ast.parse(expression).body[0], filename='<ast>', mode='eval'))
if __name__ == '__main__':
    expression1 = 'True'
    expression2 = 'False'
    expression3 = '1 == 1'
    expression4 = '2 > 3'
    print(evaluate_boolean_expression(expression1))
    print(evaluate_boolean_expression(expression2))
    print(evaluate_boolean_expression(expression3))
    print(evaluate_boolean_expression(expression4))