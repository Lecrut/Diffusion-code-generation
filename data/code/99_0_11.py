def evaluate_expression(expression: str) -> float:
    def parse_expression(pos: int) -> tuple:
        result, pos = parse_term(pos)
        while pos < len(expression) and expression[pos] in ('+', '-'):
            op = expression[pos]
            pos += 1
            right, pos = parse_term(pos)
            if op == '+':
                result += right
            else:
                result -= right
        return result, pos

    def parse_term(pos: int) -> tuple:
        result, pos = parse_factor(pos)
        while pos < len(expression) and expression[pos] in ('*', '/'):
            op = expression[pos]
            pos += 1
            right, pos = parse_factor(pos)
            if op == '*':
                result *= right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                result /= right
        return result, pos

    def parse_factor(pos: int) -> tuple:
        if pos < len(expression) and expression[pos] == '-':
            pos += 1
            val, pos = parse_factor(pos)
            return -val, pos
        if pos < len(expression) and expression[pos] == '+':
            pos += 1
            val, pos = parse_factor(pos)
            return val, pos
        if pos < len(expression) and expression[pos] == '(':
            pos += 1
            val, pos = parse_expression(pos)
            if pos < len(expression) and expression[pos] == ')':
                pos += 1
            return val, pos
        num_str = []
        while pos < len(expression) and (expression[pos].isdigit() or expression[pos] == '.'):
            num_str.append(expression[pos])
            pos += 1
        if not num_str:
            raise ValueError(f"Unexpected character at position {pos}: {expression[pos] if pos < len(expression) else 'end of string'}")
        return float(num_str), pos

    pos = 0
    result, pos = parse_expression(pos)
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))
    print(evaluate_expression("10 / 2 + 3"))
    print(evaluate_expression("(1 + 2) * (3 + 4)"))
    print(evaluate_expression("-5 + 10"))
    print(evaluate_expression("100"))