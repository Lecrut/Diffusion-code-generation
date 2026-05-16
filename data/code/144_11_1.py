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
        for var, value in variables.items():
            if len(var) > 1 and var in expr:
                if expr.count(var) == 1 and (expr.startswith(var + ' ') or expr.startswith(var) and len(expr) == len(var)):
                    expr = expr.replace(var, str(value), 1)
        try:
            result = eval(expr)
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
    expr2 = '(P OR Q) NOT P'
    result2 = evaluate_expression(P_val, Q_val, expr2)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr2}' -> Result: {result2}")
    expr3 = 'NOT (P AND Q)'
    result3 = evaluate_expression(P_val, Q_val, expr3)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr3}' -> Result: {result3}")
    expr4 = 'P OR (NOT Q)'
    result4 = evaluate_expression(P_val, Q_val, expr4)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr4}' -> Result: {result4}")
    expr5 = 'P AND P'
    result5 = evaluate_expression(P_val, Q_val, expr5)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr5}' -> Result: {result5}")
    expr6 = '(P OR Q) AND (NOT P)'
    result6 = evaluate_expression(P_val, Q_val, expr6)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr6}' -> Result: {result6}")