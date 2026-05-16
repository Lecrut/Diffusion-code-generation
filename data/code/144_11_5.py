import re
def evaluate_expression(P, Q, expression):
    variables = {'P': P, 'Q': Q}
    def _eval(expr):
        expr = expr.strip()
        if not expr:
            return None
        if expr == 'P':
            return variables['P']
        elif expr == 'Q':
            return variables['Q']
        elif expr == 'AND':
            return variables['P'] and variables['Q']
        elif expr == 'OR':
            return variables['P'] or variables['Q']
        elif expr == 'NOT':
            return not variables['P']
        elif expr == '(':
            return _eval(expr[1:])
        elif expr == ')':
            return None
        else:
            try:
                result = eval(expr)
                if isinstance(result, bool):
                    return result
                return result
            except Exception:
                return None
    try:
        return _eval(expression)
    except Exception:
        return False
if __name__ == '__main__':
    P_val = True
    Q_val = False
    expression1 = 'P AND Q'
    result1 = evaluate_expression(P_val, Q_val, expression1)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expression1}', Result: {result1}")
    expression2 = '(P OR Q) NOT P'
    result2 = evaluate_expression(P_val, Q_val, expression2)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expression2}', Result: {result2}")
    expression3 = 'NOT (P AND NOT Q)'
    result3 = evaluate_expression(P_val, Q_val, expression3)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expression3}', Result: {result3}")
    expression4 = 'P OR Q'
    result4 = evaluate_expression(P_val, Q_val, expression4)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expression4}', Result: {result4}")