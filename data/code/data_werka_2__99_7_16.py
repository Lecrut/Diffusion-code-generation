def evaluate_boolean_expression(expression: str) -> bool:
    try:
        allowed_names = {'True': True, 'False': False, 'and': lambda x, y: x and y, 'or': lambda x, y: x or y, 'not': lambda x: not x, 'True': True, 'False': False, 'None': None, 'True': True, 'False': False}
        safe_globals = {'__builtins__': {'True': True, 'False': False, 'None': None, 'bool': bool, 'int': int, 'float': float, 'str': str, 'len': len, 'abs': abs, 'min': min, 'max': max, 'sum': sum, 'any': any, 'all': all}}
        result = eval(expression, safe_globals, {})
        if not isinstance(result, bool):
            return bool(result)
        return result
    except SyntaxError:
        raise ValueError('Invalid syntax in boolean expression')
    except Exception as e:
        raise ValueError(f'Error evaluating expression: {e}')
if __name__ == '__main__':
    print(evaluate_boolean_expression('True and False'))
    print(evaluate_boolean_expression('True or False'))
    print(evaluate_boolean_expression('not True'))
    print(evaluate_boolean_expression('1 == 1 and 2 > 1'))
    print(evaluate_boolean_expression('(10 > 5) and (3 < 4)'))
    print(evaluate_boolean_expression('True and (False or True)'))