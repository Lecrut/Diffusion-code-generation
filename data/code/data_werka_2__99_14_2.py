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
        elif char in ('(', ')'):
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        else:
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
            value, index = parse_not(index)
            return not value, index
        return parse_primary(index)

    def parse_primary(index):
        if index < len(tokens) and tokens[index] == '(':
            index += 1
            value, index = parse_or(index)
            if index < len(tokens) and tokens[index] == ')':
                index += 1
            return value, index
        value_str = tokens[index]
        index += 1
        if value_str == 'TRUE':
            return True, index
        elif value_str == 'FALSE':
            return False, index
        else:
            raise ValueError(f"Unknown token: {value_str}")

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
        "NOT NOT TRUE",
        "TRUE AND TRUE AND FALSE",
        "FALSE OR TRUE OR FALSE"
    ]
    for expr in expressions:
        result = evaluate_expression(expr)
        print(result)