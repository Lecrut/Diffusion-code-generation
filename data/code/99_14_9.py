def evaluate_expression(expression: str) -> bool:
    tokens = []
    current = []
    for char in expression:
        if char.isspace():
            if current:
                tokens.append(''.join(current))
                current = []
        elif char in '()':
            if current:
                tokens.append(''.join(current))
                current = []
            tokens.append(char)
        else:
            current.append(char)
    if current:
        tokens.append(''.join(current))
    
    def parse_or(idx):
        left, idx = parse_and(idx)
        while idx < len(tokens) and tokens[idx].upper() == 'OR':
            idx += 1
            right, idx = parse_and(idx)
            left = left or right
        return left, idx

    def parse_and(idx):
        left, idx = parse_not(idx)
        while idx < len(tokens) and tokens[idx].upper() == 'AND':
            idx += 1
            right, idx = parse_not(idx)
            left = left and right
        return left, idx

    def parse_not(idx):
        if idx < len(tokens) and tokens[idx].upper() == 'NOT':
            idx += 1
            val, idx = parse_not(idx)
            return not val, idx
        return parse_primary(idx)

    def parse_primary(idx):
        if idx >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token = tokens[idx]
        if token == '(':
            idx += 1
            val, idx = parse_or(idx)
            if idx >= len(tokens) or tokens[idx] != ')':
                raise ValueError("Missing closing parenthesis")
            return val, idx + 1
        if token.upper() == 'TRUE':
            return True, idx + 1
        if token.upper() == 'FALSE':
            return False, idx + 1
        raise ValueError(f"Unknown token: {token}")

    result, end_idx = parse_or(0)
    if end_idx != len(tokens):
        raise ValueError("Unexpected tokens at end of expression")
    return result

if __name__ == '__main__':
    expr = "True AND (False OR NOT False)"
    result = evaluate_expression(expr)
    print(result)