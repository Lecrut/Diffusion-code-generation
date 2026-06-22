def evaluate_expression(expression: str) -> bool:
    tokens = []
    current_token = ""
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == ' ':
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
        current_token += char
        i += 1
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
            val, index = parse_not(index)
            return not val, index
        return parse_primary(index)

    def parse_primary(index):
        if index < len(tokens) and tokens[index] == '(':
            index += 1
            val, index = parse_or(index)
            if index < len(tokens) and tokens[index] == ')':
                index += 1
            return val, index
        val_str = tokens[index]
        index += 1
        if val_str == 'TRUE':
            return True, index
        if val_str == 'FALSE':
            return False, index
        raise ValueError(f"Unknown token: {val_str}")

    result, _ = parse_or(0)
    return result

if __name__ == '__main__':
    expressions = [
        "TRUE AND FALSE OR TRUE",
        "NOT FALSE AND TRUE",
        "TRUE OR FALSE AND FALSE",
        "(TRUE OR FALSE) AND FALSE",
        "NOT (TRUE AND FALSE)",
        "TRUE AND TRUE AND FALSE",
        "FALSE OR FALSE OR TRUE"
    ]
    for expr in expressions:
        result = evaluate_expression(expr)
        print(result)