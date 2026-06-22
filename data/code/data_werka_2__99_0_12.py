def evaluate_expression(expression: str) -> float:
    def parse_expression(pos: int) -> tuple:
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

    def parse_term(pos: int) -> tuple:
        left, pos = parse_factor(pos)
        while pos < len(expression) and expression[pos] in ('*', '/'):
            op = expression[pos]
            pos += 1
            right, pos = parse_factor(pos)
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                left = left / right
        return left, pos

    def parse_factor(pos: int) -> tuple:
        if pos < len(expression) and expression[pos] == '-':
            pos += 1
            value, pos = parse_factor(pos)
            return -value, pos
        if pos < len(expression) and expression[pos] == '+':
            pos += 1
            value, pos = parse_factor(pos)
            return value, pos
        if pos < len(expression) and expression[pos] == '(':
            pos += 1
            value, pos = parse_expression(pos)
            if pos < len(expression) and expression[pos] == ')':
                pos += 1
            return value, pos
        return parse_number(pos)

    def parse_number(pos: int) -> tuple:
        start = pos
        while pos < len(expression) and (expression[pos].isdigit() or expression[pos] == '.'):
            pos += 1
        if start == pos:
            raise ValueError(f"Unexpected character at position {pos}: {expression[pos] if pos < len(expression) else 'end of string'}")
        num_str = expression[start:pos]
        if '.' in num_str:
            return float(num_str), pos
        return int(num_str), pos

    pos = 0
    result, pos = parse_expression(pos)
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))
    print(evaluate_expression("10 / 2 + 3"))
    print(evaluate_expression("(1 + 2) * (3 + 4)"))
    print(evaluate_expression("-5 + 10"))
    print(evaluate_expression("2 ** 3 + 4"))