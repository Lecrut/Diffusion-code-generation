def evaluate_boolean_expression(expression: str) -> bool:
    try:
        allowed_names = {'True': True, 'False': False, 'and': lambda x, y: x and y, 'or': lambda x, y: x or y, 'not': lambda x: not x, 'True': True, 'False': False}
        safe_globals = {'__builtins__': {}, 'True': True, 'False': False}
        result = eval(expression, safe_globals, {})
        return bool(result)
    except SyntaxError:
        raise ValueError(f'Invalid syntax in expression: {expression}')
    except Exception as e:
        raise ValueError(f'Error evaluating expression: {expression}') from e
if __name__ == '__main__':
    expr1 = 'True and False'
    expr2 = '1 > 2 or 3 == 3'
    expr3 = 'not (5 < 10)'
    expr4 = 'True or False and False'
    print(evaluate_boolean_expression(expr1))
    print(evaluate_boolean_expression(expr2))
    print(evaluate_boolean_expression(expr3))
    print(evaluate_boolean_expression(expr4))