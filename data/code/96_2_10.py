def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
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
        elif char == '!':
            if i + 1 < n and expression[i + 1] == '=':
                tokens.append('!=')
                i += 2
            else:
                raise ValueError(f'Unsupported operator at index {i}')
        elif char.isalpha() or char == '_':
            j = i
            while j < n and (expression[j].isalnum() or expression[j] == '_'):
                j += 1
            word = expression[i:j]
            if word in ('and', 'or', 'not'):
                tokens.append(word)
            elif word in ('true', 'false'):
                tokens.append(word.lower())
            else:
                tokens.append(word)
            i = j
        elif char.isdigit():
            j = i
            while j < n and expression[j].isdigit():
                j += 1
            tokens.append(expression[i:j])
            i = j
        else:
            raise ValueError(f'Unexpected character: {char}')
    result, _ = _parse_expr(tokens, 0)
    return result

def _parse_expr(tokens, pos):
    left, pos = _parse_and(tokens, pos)
    while pos < len(tokens) and tokens[pos] == 'or':
        pos += 1
        right, pos = _parse_and(tokens, pos)
        left = left or right
    return (left, pos)

def _parse_and(tokens, pos):
    left, pos = _parse_not(tokens, pos)
    while pos < len(tokens) and tokens[pos] == 'and':
        pos += 1
        right, pos = _parse_not(tokens, pos)
        left = left and right
    return (left, pos)

def _parse_not(tokens, pos):
    if pos < len(tokens) and tokens[pos] == 'not':
        pos += 1
        val, pos = _parse_not(tokens, pos)
        return (not val, pos)
    return _parse_atom(tokens, pos)

def _parse_atom(tokens, pos):
    if pos >= len(tokens):
        raise ValueError('Unexpected end of expression')
    token = tokens[pos]
    if token == '(':
        pos += 1
        val, pos = _parse_expr(tokens, pos)
        if pos >= len(tokens) or tokens[pos] != ')':
            raise ValueError('Missing closing parenthesis')
        pos += 1
        return (val, pos)
    elif token == 'true':
        return (True, pos + 1)
    elif token == 'false':
        return (False, pos + 1)
    elif token in ('and', 'or', ')'):
        raise ValueError(f'Unexpected token: {token}')
    elif token.isalnum():
        if token in ('true', 'false'):
            return (token == 'true', pos + 1)
        elif token.isdigit():
            return (int(token) != 0, pos + 1)
        else:
            if token not in variables:
                raise ValueError(f'Undefined variable: {token}')
            val = variables[token]
            if isinstance(val, bool):
                return (val, pos + 1)
            elif isinstance(val, (int, float)):
                return (bool(val), pos + 1)
            else:
                return (bool(val), pos + 1)
    else:
        raise ValueError(f'Unknown token: {token}')
if __name__ == '__main__':
    assert evaluate_boolean_expression('true and false', {'a': True}) == False
    assert evaluate_boolean_expression('true or false', {'a': True}) == True
    assert evaluate_boolean_expression('not true', {'a': True}) == False
    assert evaluate_boolean_expression('a and b', {'a': True, 'b': False}) == False
    assert evaluate_boolean_expression('(true or false) and true', {'a': True}) == True