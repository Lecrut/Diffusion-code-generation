def evaluate_expression(expression: str) -> float:
    def parse_expression(pos: int):
        left, pos = parse_term(pos)
        while pos < len(expression) and expression[pos] in ('+', '-'):
            op = expression[pos]
            pos += 1
            right, pos = parse_term(pos)
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left, pos

    def parse_term(pos: int):
        left, pos = parse_factor(pos)
        while pos < len(expression) and expression[pos] in ('*', '/'):
            op = expression[pos]
            pos += 1
            right, pos = parse_factor(pos)
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                left = left / right
        return left, pos

    def parse_factor(pos: int):
        if pos < len(expression) and expression[pos] == '(':
            pos += 1
            val, pos = parse_expression(pos)
            if pos >= len(expression) or expression[pos] != ')':
                raise ValueError("Mismatched parentheses")
            pos += 1
            return val, pos
        
        if pos < len(expression) and expression[pos] == '-':
            val, pos = parse_factor(pos + 1)
            return -val, pos
        
        if pos < len(expression) and expression[pos] == '+':
            val, pos = parse_factor(pos + 1)
            return val, pos

        start = pos
        while pos < len(expression) and (expression[pos].isdigit() or expression[pos] == '.'):
            pos += 1
        
        if start == pos:
            raise ValueError(f"Unexpected character at position {pos}: {expression[pos] if pos < len(expression) else 'end'}")
        
        num_str = expression[start:pos]
        if '.' in num_str:
            return float(num_str), pos
        return int(num_str), pos

    pos = 0
    result, pos = parse_expression(pos)
    if pos < len(expression):
        raise ValueError(f"Unexpected character at position {pos}: {expression[pos]}")
    return result

if __name__ == '__main__':
    expr1 = "3 + 5 * (2 - 8)"
    result1 = evaluate_expression(expr1)
    print(result1)

    expr2 = "10 / 2 + 3 * 4"
    result2 = evaluate_expression(expr2)
    print(result2)

    expr3 = "(1 + 2) * (3 + 4)"
    result3 = evaluate_expression(expr3)
    print(result3)

    expr4 = "-5 + 10"
    result4 = evaluate_expression(expr4)
    print(result4)