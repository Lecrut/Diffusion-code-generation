def evaluate_parenthesized_expression(expression: str) -> float:
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty expression")
    
    def parse():
        val = parse_factor()
        while pos < len(expression) and expression[pos] in '+-':
            op = expression[pos]
            pos += 1
            right = parse_factor()
            if op == '+':
                val = val + right
            else:
                val = val - right
        return val

    def parse_factor():
        val = parse_term()
        while pos < len(expression) and expression[pos] in '*/':
            op = expression[pos]
            pos += 1
            right = parse_term()
            if op == '*':
                val = val * right
            else:
                val = val / right
        return val

    def parse_term():
        if pos < len(expression) and expression[pos] == '(':
            pos += 1
            val = parse()
            if pos < len(expression) and expression[pos] == ')':
                pos += 1
                return val
            else:
                raise ValueError("Missing closing parenthesis")
        
        num_str = []
        while pos < len(expression) and (expression[pos].isdigit() or expression[pos] == '.'):
            num_str.append(expression[pos])
            pos += 1
        
        if not num_str:
            raise ValueError("Expected number or parenthesis")
        
        num_val = float(''.join(num_str))
        if '.' in num_str:
            return num_val
        return int(num_val)

    pos = 0
    result = parse()
    if pos < len(expression):
        raise ValueError("Unexpected trailing characters")
    return result

if __name__ == '__main__':
    expr1 = "(1 + (2 * 3))"
    result1 = evaluate_parenthesized_expression(expr1)
    print(result1)
    
    expr2 = "((10 / 2) - (3 + 1))"
    result2 = evaluate_parenthesized_expression(expr2)
    print(result2)
    
    expr3 = "((2 + 3) * (4 - 1))"
    result3 = evaluate_parenthesized_expression(expr3)
    print(result3)