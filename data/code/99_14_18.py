def evaluate_expression(expression: str) -> bool:
    tokens = []
    current_token = ""
    for char in expression:
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif char in "(),":
            if current_token:
                tokens.append(current_token)
                current_token = ""
            if char == "(":
                tokens.append("(")
            elif char == ")":
                tokens.append(")")
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)

    def parse_or(tokens, pos):
        left, pos = parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos] == "OR":
            pos += 1
            right, pos = parse_and(tokens, pos)
            left = left or right
        return left, pos

    def parse_and(tokens, pos):
        left, pos = parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos] == "AND":
            pos += 1
            right, pos = parse_not(tokens, pos)
            left = left and right
        return left, pos

    def parse_not(tokens, pos):
        if pos < len(tokens) and tokens[pos] == "NOT":
            pos += 1
            val, pos = parse_not(tokens, pos)
            return not val, pos
        return parse_primary(tokens, pos)

    def parse_primary(tokens, pos):
        if pos < len(tokens) and tokens[pos] == "(":
            pos += 1
            val, pos = parse_or(tokens, pos)
            if pos < len(tokens) and tokens[pos] == ")":
                pos += 1
            return val, pos
        val_str = tokens[pos]
        pos += 1
        if val_str == "TRUE":
            return True, pos
        if val_str == "FALSE":
            return False, pos
        raise ValueError(f"Unknown token: {val_str}")

    result, _ = parse_or(tokens, 0)
    return result

if __name__ == '__main__':
    expr1 = "TRUE AND FALSE OR TRUE"
    expr2 = "NOT FALSE AND TRUE"
    expr3 = "(TRUE OR FALSE) AND (NOT FALSE)"
    expr4 = "NOT (TRUE AND FALSE)"
    print(evaluate_expression(expr1))
    print(evaluate_expression(expr2))
    print(evaluate_expression(expr3))
    print(evaluate_expression(expr4))