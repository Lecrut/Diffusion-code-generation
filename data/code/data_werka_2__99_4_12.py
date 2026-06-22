def parse_expression(s):
    s = s.strip()
    if not s:
        raise ValueError("Empty expression")
    
    if s.startswith('('):
        depth = 0
        split_index = -1
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
                if depth == 0:
                    split_index = i
                    break
            elif depth == 1 and char in '+-':
                split_index = i
                break
            elif depth == 1 and char in '*/':
                split_index = i
                break
        
        if split_index == -1:
            raise ValueError("Invalid parentheses structure")
        
        inner_expr = s[1:split_index]
        operator = s[split_index]
        right_expr = s[split_index + 1:].strip()
        
        if not right_expr.endswith(')'):
            raise ValueError("Missing closing parenthesis")
        
        left_val = parse_expression(inner_expr)
        right_val = parse_expression(right_expr)
        
        if operator == '+':
            return left_val + right_val
        elif operator == '-':
            return left_val - right_val
        elif operator == '*':
            return left_val * right_val
        elif operator == '/':
            if right_val == 0:
                raise ValueError("Division by zero")
            return left_val / right_val
        else:
            raise ValueError(f"Unsupported operator: {operator}")
    else:
        try:
            return float(s)
        except ValueError:
            raise ValueError(f"Invalid number: {s}")

if __name__ == '__main__':
    expression = "((10+2)*(3-1))"
    result = parse_expression(expression)
    print(result)