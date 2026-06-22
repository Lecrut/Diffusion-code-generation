def evaluate_expression(expression: str) -> bool:
    tokens = []
    current_token = ""
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
            i += 1
            continue
        if char in ('(', ')'):
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
            i += 1
            continue
        if char.isalpha() or char.isdigit():
            current_token += char
            i += 1
            continue
        raise ValueError(f"Unsupported character: {char}")
    if current_token:
        tokens.append(current_token)

    def parse_or(index):
        left, index = parse_and(index)
        while index < len(tokens) and tokens[index] == 'OR':
            index += 1
            right, index = parse_and(index)
            left = left or right
        return left, index

    def parse_and(index):
        left, index = parse_not(index)
        while index < len(tokens) and tokens[index] == 'AND':
            index += 1
            right, index = parse_not(index)
            left = left and right
        return left, index

    def parse_not(index):
        if index < len(tokens) and tokens[index] == 'NOT':
            index += 1
            value, index = parse_not(index)
            return not value, index
        return parse_primary(index)

    def parse_primary(index):
        if index >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token = tokens[index]
        if token == '(':
            index += 1
            value, index = parse_or(index)
            if index >= len(tokens) or tokens[index] != ')':
                raise ValueError("Missing closing parenthesis")
            index += 1
            return value, index
        if token == 'TRUE':
            return True, index + 1
        if token == 'FALSE':
            return False, index + 1
        if token in ('AND', 'OR', ')'):
            raise ValueError(f"Unexpected token: {token}")
        raise ValueError(f"Unknown token: {token}")

    result, end_index = parse_or(0)
    if end_index != len(tokens):
        raise ValueError("Unexpected tokens at end of expression")
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
        "NOT NOT TRUE",
        "TRUE AND TRUE AND FALSE",
        "FALSE OR TRUE OR FALSE"
    ]
    for expr in expressions:
        result = evaluate_expression(expr)
        print(result)