import re
def evaluate_expression(P, Q, expression):
    variables = {'P': P, 'Q': Q}
    def _eval_tokens(tokens):
        if not tokens:
            return None
        if tokens[0].isalnum():
            return variables.get(tokens[0], tokens[0])
        if tokens[0] == '(':
            balance = 1
            sub_expression = []
            i = 1
            while i < len(tokens):
                if tokens[i] == '(':
                    balance += 1
                elif tokens[i] == ')':
                    balance -= 1
                if balance == 0:
                    sub_expression = tokens[1:i+1]
                    break
                i += 1
            if balance == 0:
                sub_result = _eval_tokens(sub_expression)
                if sub_result is not None:
                    return sub_result
            return None
        if tokens[0] in ('NOT', 'AND', 'OR'):
            operator = tokens[0]
            operand = _eval_tokens(tokens[1])
            if operand is None:
                raise ValueError("Invalid expression structure")
            if operator == 'NOT':
                return not operand
            elif operator == 'AND':
                return operand and variables.get('P', False) and variables.get('Q', False)                                     
            elif operator == 'OR':
                return operand or variables.get('P', False) or variables.get('Q', False)                                     
        return variables.get(tokens[0], tokens[0])
    processed_expression = expression.upper().replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')
    tokens = processed_expression.split()
    final_tokens = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '(':
            final_tokens.append(token)
            i += 1
        elif token == ')':
            final_tokens.append(token)
            i += 1
        elif token in ('AND', 'OR', 'NOT'):
            final_tokens.append(token)
            i += 1
        else:
            final_tokens.append(token)
            i += 1
    safe_expression = expression.replace('P', str(P)).replace('Q', str(Q))
    try:
        result = eval(safe_expression)
        return bool(result)
    except Exception:
        return False
if __name__ == '__main__':
    P_val = True
    Q_val = False
    expressions = [
        'P AND Q',
        '(P OR Q) NOT P',
        'NOT P OR Q',
        'P AND (Q OR NOT P)'
    ]
    print(f"P = {P_val}, Q = {Q_val}\n")
    for expr in expressions:
        result = evaluate_expression(P_val, Q_val, expr)
        print(f"Expression: '{expr}' -> Result: {result}")
        print("-" * 20)