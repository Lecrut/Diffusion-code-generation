def evaluate_boolean_expression(expression, variables):
    import re
    def solve(sub_expression):
        if sub_expression.startswith('(') and sub_expression.endswith(')'):
            content = sub_expression[1:-1]
            balance = 0
            result_parts = []
            start = 0
            for i, char in enumerate(content):
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if balance == 0:
                    part = content[start:i+1].strip()
                    if ' and ' in part or ' or ' in part:
                        parts = re.split(r'\s+(and|or)\s+', part)
                        if len(parts) == 3:
                            left_var = parts[0].strip()
                            op = parts[1].strip()
                            right_var = parts[2].strip()
                            left_val = solve(left_var)
                            right_val = solve(right_var)
                            if op == 'and':
                                result_parts.append(left_val and right_val)
                            elif op == 'or':
                                result_parts.append(left_val or right_val)
                    start = i + 1
            if not result_parts:
                return None
            return result_parts[0] if result_parts else False
        if sub_expression in variables:
            return variables[sub_expression]
        if sub_expression in variables:
            return variables[sub_expression]
        return None
    processed_expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    tokens = [t for t in processed_expression.split() if t]
    def recursive_eval(expr):
        expr = expr.strip()
        if expr in variables:
            return variables[expr]
        if expr.startswith('(') and expr.endswith(')'):
            content = expr[1:-1].strip()
            balance = 0
            split_index = -1
            operator = None
            for i in range(len(content) - 1, -1, -1):
                char = content[i]
                if char == ')':
                    balance += 1
                elif char == '(':
                    balance -= 1
                elif balance == 0:
                    if content[i:i+4] == ' and ':
                        split_index = i
                        operator = 'and'
                        break
                    elif content[i:i+4] == ' or ':
                        split_index = i
                        operator = 'or'
                        break
            if split_index != -1:
                left_expr = content[:split_index].strip()
                right_expr = content[split_index+4:].strip()
                left_val = recursive_eval(left_expr)
                right_val = recursive_eval(right_expr)
                if left_val is not None and right_val is not None:
                    if operator == 'and':
                        return left_val and right_val
                    elif operator == 'or':
                        return left_val or right_val
            return None
        return None
    return recursive_eval(expression)
if __name__ == '__main__':
    variables = {
        'A': True,
        'B': False,
        'C': True
    }
    expression1 = '((A and B) or C)'
    result1 = evaluate_boolean_expression(expression1, variables)
    print(f"Expression: {expression1}")
    print(f"Variables: {variables}")
    print(f"Result: {result1}")
    print("-" * 20)
    variables2 = {
        'X': True,
        'Y': False,
        'Z': True
    }
    expression2 = '(X or (Y and Z))'
    result2 = evaluate_boolean_expression(expression2, variables2)
    print(f"Expression: {expression2}")
    print(f"Variables: {variables2}")
    print(f"Result: {result2}")
    print("-" * 20)
    variables3 = {
        'P': True,
        'Q': False
    }
    expression3 = '((P and Q) or P)'
    result3 = evaluate_boolean_expression(expression3, variables3)
    print(f"Expression: {expression3}")
    print(f"Variables: {variables3}")
    print(f"Result: {result3}")