def evaluate_expression(expression: str) -> float:
    def parse_expression():
        return parse_addition()

    def parse_addition():
        left = parse_multiplication()
        while True:
            skip_spaces()
            if not tokens or tokens[0] not in ('+', '-'):
                break
            op = tokens.pop(0)
            right = parse_multiplication()
            if op == '+':
                left = left + right
            else:
                left = left - right
        return left

    def parse_multiplication():
        left = parse_unary()
        while True:
            skip_spaces()
            if not tokens or tokens[0] not in ('*', '/'):
                break
            op = tokens.pop(0)
            right = parse_unary()
            if op == '*':
                left = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError("division by zero")
                left = left / right
        return left

    def parse_unary():
        skip_spaces()
        if not tokens:
            raise ValueError("Unexpected end of expression")
        if tokens[0] == '-':
            tokens.pop(0)
            operand = parse_unary()
            return -operand
        if tokens[0] == '+':
            tokens.pop(0)
            return parse_unary()
        return parse_primary()

    def parse_primary():
        skip_spaces()
        if not tokens:
            raise ValueError("Unexpected end of expression")
        token = tokens[0]
        if token == '(':
            tokens.pop(0)
            result = parse_expression()
            skip_spaces()
            if not tokens or tokens[0] != ')':
                raise ValueError("Missing closing parenthesis")
            tokens.pop(0)
            return result
        if isinstance(token, (int, float)):
            tokens.pop(0)
            return float(token)
        raise ValueError(f"Unexpected token: {token}")

    def skip_spaces():
        while tokens and tokens[0] == ' ':
            tokens.pop(0)

    def tokenize(expr: str):
        tokens_list = []
        i = 0
        n = len(expr)
        while i < n:
            c = expr[i]
            if c == ' ':
                i += 1
                continue
            if c in '+-*/()':
                tokens_list.append(c)
                i += 1
                continue
            if c.isdigit() or c == '.':
                j = i
                has_dot = False
                while j < n and (expr[j].isdigit() or expr[j] == '.'):
                    if expr[j] == '.':
                        if has_dot:
                            raise ValueError("Invalid number format")
                        has_dot = True
                    j += 1
                num_str = expr[i:j]
                if has_dot:
                    tokens_list.append(float(num_str))
                else:
                    tokens_list.append(int(num_str))
                i = j
                continue
            raise ValueError(f"Unexpected character: {c}")
        return tokens_list

    tokens = tokenize(expression)
    if not tokens:
        raise ValueError("Empty expression")
    result = parse_expression()
    skip_spaces()
    if tokens:
        raise ValueError(f"Unexpected token after expression: {tokens[0]}")
    return result

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))
    print(evaluate_expression("10 / 2 + 3"))
    print(evaluate_expression("(1 + 2) * (3 + 4)"))
    print(evaluate_expression("-3 + 4"))
    print(evaluate_expression("((2))"))