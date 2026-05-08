import re
def evaluate_expression(P, Q, expression):
    variables = {'P': P, 'Q': Q}
    def _eval(expr):
        expr = expr.strip()
        if not expr:
            return None
        expr = expr.replace('AND', 'and')
        expr = expr.replace('OR', 'or')
        expr = expr.replace('NOT', 'not')
        try:
            result = eval(expr, {}, variables)
            return result
        except Exception:
            return False
    return _eval(expression)
if __name__ == '__main__':
    P_val = True
    Q_val = False
    expr1 = 'P AND Q'
    result1 = evaluate_expression(P_val, Q_val, expr1)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr1}' -> Result: {result1}")
    expr2 = 'P OR Q'
    result2 = evaluate_expression(P_val, Q_val, expr2)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr2}' -> Result: {result2}")
    expr3 = 'NOT P'
    result3 = evaluate_expression(P_val, Q_val, expr3)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr3}' -> Result: {result3}")
    expr4 = '(P OR Q) NOT P'
    result4 = evaluate_expression(P_val, Q_val, expr4)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr4}' -> Result: {result4}")
    P_val_2 = False
    Q_val_2 = True
    expr5 = 'P AND Q'
    result5 = evaluate_expression(P_val_2, Q_val_2, expr5)
    print(f"P={P_val_2}, Q={Q_val_2}, Expression: '{expr5}' -> Result: {result5}")