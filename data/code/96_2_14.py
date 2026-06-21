def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    expression = expression.strip()
    if not expression:
        raise ValueError('Empty expression')
    tokens = []
    i = 0
    n = len(expression)
    while i < n:
        char = expression[i]
        if char.isspace():
            i += 1
            continue
        if char == '(':
            tokens.append('(')
            i += 1
        elif char == ')':
            tokens.append(')')
            i += 1
        elif char == 'a' and i + 3 < n and (expression[i:i + 4] == 'and '):
            tokens.append('and')
            i += 4
        elif char == 'a' and i + 2 < n and (expression[i:i + 3] == 'and'):
            tokens.append('and')
            i += 3
        elif char == 'o' and i + 1 < n and (expression[i:i + 2] == 'or'):
            tokens.append('or')
            i += 2
        elif char == 'n' and i + 2 < n and (expression[i:i + 3] == 'not'):
            tokens.append('not')
            i += 3
        elif char.isalpha() or char == '_':
            start = i
            while i < n and (expression[i].isalnum() or expression[i] == '_'):
                i += 1
            tokens.append(expression[start:i])
        else:
            raise ValueError(f'Unexpected character: {char}')
    if not tokens:
        raise ValueError('No tokens found')
    result, _ = parse_or(tokens, 0)
    return result

def parse_or(tokens, pos):
    left, pos = parse_and(tokens, pos)
    while pos < len(tokens) and tokens[pos] == 'or':
        pos += 1
        right, pos = parse_and(tokens, pos)
        left = left or right
    return (left, pos)

def parse_and(tokens, pos):
    left, pos = parse_not(tokens, pos)
    while pos < len(tokens) and tokens[pos] == 'and':
        pos += 1
        right, pos = parse_not(tokens, pos)
        left = left and right
    return (left, pos)

def parse_not(tokens, pos):
    if pos < len(tokens) and tokens[pos] == 'not':
        pos += 1
        val, pos = parse_not(tokens, pos)
        return (not val, pos)
    return parse_primary(tokens, pos)

def parse_primary(tokens, pos):
    if pos >= len(tokens):
        raise ValueError('Unexpected end of expression')
    token = tokens[pos]
    if token == '(':
        pos += 1
        val, pos = parse_or(tokens, pos)
        if pos >= len(tokens) or tokens[pos] != ')':
            raise ValueError('Missing closing parenthesis')
        pos += 1
        return (val, pos)
    elif token == 'True':
        return (True, pos + 1)
    elif token == 'False':
        return (False, pos + 1)
    elif token in variables:
        return (bool(variables[token]), pos + 1)
    else:
        raise ValueError(f'Unknown token: {token}')
if __name__ == '__main__':
    assert evaluate_boolean_expression('x', {'x': True}) == True
    assert evaluate_boolean_expression('x', {'x': False}) == False
    assert evaluate_boolean_expression('x and y', {'x': True, 'y': True}) == True
    assert evaluate_boolean_expression('x and y', {'x': True, 'y': False}) == False
    assert evaluate_boolean_expression('x and y', {'x': False, 'y': True}) == False
    assert evaluate_boolean_expression('x and y', {'x': False, 'y': False}) == False
    assert evaluate_boolean_expression('x or y', {'x': True, 'y': True}) == True
    assert evaluate_boolean_expression('x or y', {'x': True, 'y': False}) == True
    assert evaluate_boolean_expression('x or y', {'x': False, 'y': True}) == True
    assert evaluate_boolean_expression('x or y', {'x': False, 'y': False}) == False
    assert evaluate_boolean_expression('not x', {'x': True}) == False