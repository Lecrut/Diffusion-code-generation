def evaluate_expression(expr: str) -> bool:
    tokens = []
    current = ""
    for char in expr:
        if char in " \t\n\r":
            if current:
                tokens.append(current)
                current = ""
        else:
            current += char
    if current:
        tokens.append(current)

    def parse_or(index):
        left, index = parse_and(index)
        while index < len(tokens) and tokens[index] == "OR":
            index += 1
            right, index = parse_and(index)
            left = left or right
        return left, index

    def parse_and(index):
        left, index = parse_not(index)
        while index < len(tokens) and tokens[index] == "AND":
            index += 1
            right, index = parse_not(index)
            left = left and right
        return left, index

    def parse_not(index):
        if index < len(tokens) and tokens[index] == "NOT":
            index += 1
            val, index = parse_not(index)
            return not val, index
        return parse_primary(index)

    def parse_primary(index):
        token = tokens[index]
        if token == "(":
            index += 1
            val, index = parse_or(index)
            if index < len(tokens) and tokens[index] == ")":
                index += 1
            return val, index
        if token == "TRUE":
            return True, index + 1
        if token == "FALSE":
            return False, index + 1
        raise ValueError(f"Unexpected token: {token}")

    result, _ = parse_or(0)
    return result

if __name__ == '__main__':
    expressions = [
        "TRUE AND FALSE",
        "TRUE OR FALSE",
        "NOT TRUE",
        "TRUE AND (FALSE OR TRUE)",
        "NOT (TRUE AND FALSE)",
        "TRUE OR FALSE AND FALSE",
        "(TRUE OR FALSE) AND FALSE",
        "NOT (TRUE OR FALSE) AND TRUE",
        "TRUE AND NOT FALSE OR FALSE",
    ]
    for expr in expressions:
        result = evaluate_expression(expr)
        print(result)