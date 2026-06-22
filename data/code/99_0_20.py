def evaluate_expression(expression: str) -> float:
    def parse_number(start):
        end = start
        has_dot = False
        while end < len(expression) and (expression[end].isdigit() or expression[end] == '.'):
            if expression[end] == '.':
                if has_dot:
                    break
                has_dot = True
            end += 1
        if end == start:
            raise ValueError("Expected number at index " + str(start))
        return float(expression[start:end]), end

    def parse_factor(pos):
        if pos >= len(expression):
            raise ValueError("Unexpected end of expression")
        char = expression[pos]
        if char == '(':
            val, pos = parse_expression(pos + 1)
            if pos >= len(expression) or expression[pos] != ')':
                raise ValueError("Missing closing parenthesis")
            return val, pos + 1
        elif char == '-':
            val, pos = parse_number(pos + 1)
            return -val, pos
        elif char == '+':
            val, pos = parse_number(pos + 1)
            return val, pos
        elif char.isdigit() or char == '.':
            return parse_number(pos)
        else:
            raise ValueError("Unexpected character: " + char)

    def parse_term(pos):
        val, pos = parse_factor(pos)
        while pos < len(expression) and expression[pos] in ('*', '/'):
            op = expression[pos]
            pos += 1
            right, pos = parse_factor(pos)
            if op == '*':
                val = val * right
            else:
                if right == 0:
                    raise ValueError("Division by zero")
                val = val / right
        return val, pos

    def parse_expression(pos):
        val, pos = parse_term(pos)
        while pos < len(expression) and expression[pos] in ('+', '-'):
            op = expression[pos]
            pos += 1
            right, pos = parse_term(pos)
            if op == '+':
                val = val + right
            else:
                val = val - right
        return val, pos

    stripped = expression.strip()
    if not stripped:
        raise ValueError("Empty expression")
    result, pos = parse_expression(0)
    if pos != len(stripped):
        raise ValueError("Unexpected characters at end of expression")
    return result

if __name__ == '__main__':
    expr1 = "3 + 5 * 2"
    result1 = evaluate_expression(expr1)
    print(result1)

    expr2 = "(10 - 2) / 4 + 1"
    result2 = evaluate_expression(expr2)
    print(result2)

    expr3 = "100 / (5 * (2 + 3))"
    result3 = evaluate_expression(expr3)
    print(result3)

    expr4 = "-5 + 10"
    result4 = evaluate_expression(expr4)
    print(result4)