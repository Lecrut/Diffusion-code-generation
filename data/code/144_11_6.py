import re
def evaluate_expression(P, Q, expression):
    variables = {'P': P, 'Q': Q}
    def _eval(expr, context):
        expr = expr.strip()
        if expr in context:
            return context[expr]
        if expr == 'True':
            return True
        if expr == 'False':
            return False
        if '(' in expr and expr.endswith(')'):
            balance = 0
            is_in_subexpr = True
            for i in range(len(expr) - 1):
                if expr[i] == '(':
                    balance += 1
                elif expr[i] == ')':
                    balance -= 1
                if balance == 0:
                    if i > 0 and expr[i-1] == '(':
                        sub_expr = expr[i:i+1]
                        result = _eval(sub_expr, context)
                        pass
            try:
                py_expr = expr.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')
                for var, val in variables.items():
                    py_expr = py_expr.replace(var, str(val))
                return eval(py_expr)
            except Exception:
                return False                  
        if expr in variables:
            return variables[expr]
        if expr == 'True':
            return True
        if expr == 'False':
            return False
        raise ValueError(f"Unrecognized expression part: {expr}")
    try:
        return _eval(expression, variables)
    except Exception:
        return False
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
    expr5 = '(P AND NOT Q) OR (NOT P AND Q)'
    result5 = evaluate_expression(P_val, Q_val, expr5)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr5}' -> Result: {result5}")
    expr6 = 'P'
    result6 = evaluate_expression(P_val, Q_val, expr6)
    print(f"P={P_val}, Q={Q_val}, Expression: '{expr6}' -> Result: {result6}")