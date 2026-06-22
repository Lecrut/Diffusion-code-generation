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
        if char == '!':
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append('NOT')
            i += 1
            continue
        if char == '&' and i + 1 < len(expression) and expression[i + 1] == '&':
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append('AND')
            i += 2
            continue
        if char == '|' and i + 1 < len(expression) and expression[i + 1] == '|':
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append('OR')
            i += 2
            continue
        if char in ('0', '1', 'T', 'F', 't', 'f', 'T', 'F'):
            current_token += char
            i += 1
            continue
        if char.isalpha():
            current_token += char
            i += 1
            continue
        raise ValueError(f"Unsupported character: {char}")
    if current_token:
        tokens.append(current_token)
    
    def parse_or(tokens, pos):
        left, pos = parse_and(tokens, pos)
        while pos < len(tokens) and tokens[pos] == 'OR':
            pos += 1
            right, pos = parse_and(tokens, pos)
            left = left or right
        return left, pos
    
    def parse_and(tokens, pos):
        left, pos = parse_not(tokens, pos)
        while pos < len(tokens) and tokens[pos] == 'AND':
            pos += 1
            right, pos = parse_not(tokens, pos)
            left = left and right
        return left, pos
    
    def parse_not(tokens, pos):
        if pos < len(tokens) and tokens[pos] == 'NOT':
            pos += 1
            val, pos = parse_not(tokens, pos)
            return not val, pos
        return parse_primary(tokens, pos)
    
    def parse_primary(tokens, pos):
        if pos >= len(tokens):
            raise ValueError("Unexpected end of expression")
        token = tokens[pos]
        if token == '(':
            pos += 1
            val, pos = parse_or(tokens, pos)
            if pos >= len(tokens) or tokens[pos] != ')':
                raise ValueError("Missing closing parenthesis")
            pos += 1
            return val, pos
        if token in ('AND', 'OR', ')'):
            raise ValueError(f"Unexpected token: {token}")
        if token in ('0', 'F', 'f'):
            return False, pos + 1
        if token in ('1', 'T', 't'):
            return True, pos + 1
        raise ValueError(f"Unknown token: {token}")
    
    result, pos = parse_or(tokens, 0)
    if pos != len(tokens):
        raise ValueError("Unexpected tokens at end of expression")
    return result

if __name__ == '__main__':
    expressions = [
        "1 AND 0 OR 1",
        "(1 OR 0) AND 0",
        "NOT 1 AND 0",
        "1 AND (0 OR 1)",
        "NOT (1 AND 0)",
        "1 OR 0 AND 0",
        "NOT NOT 1",
        "(1 OR 0) AND (0 OR 1)"
    ]
    for expr in expressions:
        result = evaluate_expression(expr)
        print(result)