def evaluate_expression(expression: str) -> float:
    def parse_number(start: int):
        end = start
        while end < len(expression) and (expression[end].isdigit() or expression[end] == '.'):
            end += 1
        return float(expression[start:end]), end

    def parse_atom(pos: int):
        while pos < len(expression) and expression[pos] == ' ':
            pos += 1
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
        else:
            val, pos = parse_number(pos)
            return val, pos

    def parse_term(start: int):
        pos = start
        pos = pos
        val, pos = parse_atom(pos)
        while pos < len(expression) and expression[pos] not in ('+', '-', ')', ' '):
            if expression[pos] in ('*', '/'):
                op = expression[pos]
                pos += 1
                while pos < len(expression) and expression[pos] == ' ':
                    pos += 1
                right, pos = parse_atom(pos)
                if op == '*':
                    val = val * right
                else:
                    val = val / right
            else:
                break
        return val, pos

    def parse_expression(start: int):
        pos = start
        val, pos = parse_term(pos)
        while pos < len(expression) and expression[pos] in ('+', '-'):
            op = expression[pos]
            pos += 1
            while pos < len(expression) and expression[pos] == ' ':
                pos += 1
            right, pos = parse_term(pos)
            if op == '+':
                val = val + right
            else:
                val = val - right
        return val, pos

    if not expression or not expression.strip():
        raise ValueError("Empty expression")
    result, _ = parse_expression(0)
    return result

if __name__ == '__main__':
    sample_expr = "( 2 + 3 ) * 4 - 10 / 5"
    result = evaluate_expression(sample_expr)
    print(result)