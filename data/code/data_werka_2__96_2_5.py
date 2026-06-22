import re
import operator

def evaluate_boolean_expression(expression: str, variables: dict) -> bool:
    tokens = tokenize(expression)
    result, _ = parse_or(tokens, 0)
    return result

def tokenize(expression: str):
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isspace():
            i += 1
            continue
        if char == '(':
            tokens.append(('LPAREN', '('))
            i += 1
        elif char == ')':
            tokens.append(('RPAREN', ')'))
            i += 1
        elif char == 'n' and expression[i:i+4] == 'and ':
            tokens.append(('AND', 'and'))
            i += 4
        elif char == 'o' and expression[i:i+2] == 'or ':
            tokens.append(('OR', 'or'))
            i += 3
        elif char == 'n' and expression[i:i+5] == 'not ':
            tokens.append(('NOT', 'not'))
            i += 4
        elif char == 't' and expression[i:i+4] == 'true':
            tokens.append(('BOOL', True))
            i += 4
        elif char == 'f' and expression[i:i+5] == 'false':
            tokens.append(('BOOL', False))
            i += 5
        elif char.isalpha() or char == '_':
            start = i
            while i < len(expression) and (expression[i].isalnum() or expression[i] == '_'):
                i += 1
            var_name = expression[start:i]
            tokens.append(('VAR', var_name))
        else:
            raise ValueError(f"Unexpected character: {char}")
    return tokens

def parse_or(tokens, pos):
    left, pos = parse_and(tokens, pos)
    while pos < len(tokens) and tokens[pos][0] == 'OR':
        pos += 1
        right, pos = parse_and(tokens, pos)
        left = left or right
    return left, pos

def parse_and(tokens, pos):
    left, pos = parse_not(tokens, pos)
    while pos < len(tokens) and tokens[pos][0] == 'AND':
        pos += 1
        right, pos = parse_not(tokens, pos)
        left = left and right
    return left, pos

def parse_not(tokens, pos):
    if pos < len(tokens) and tokens[pos][0] == 'NOT':
        pos += 1
        val, pos = parse_not(tokens, pos)
        return not val, pos
    return parse_primary(tokens, pos)

def parse_primary(tokens, pos):
    if pos >= len(tokens):
        raise ValueError("Unexpected end of expression")
    token_type, token_val = tokens[pos]
    if token_type == 'LPAREN':
        pos += 1
        val, pos = parse_or(tokens, pos)
        if pos >= len(tokens) or tokens[pos][0] != 'RPAREN':
            raise ValueError("Missing closing parenthesis")
        pos += 1
        return val, pos
    elif token_type == 'BOOL':
        return token_val, pos + 1
    elif token_type == 'VAR':
        if token_val not in variables:
            raise ValueError(f"Undefined variable: {token_val}")
        return variables[token_val], pos + 1
    else:
        raise ValueError(f"Unexpected token: {token_val}")

if __name__ == '__main__':
    expr = '((A and B) or C)'
    vars_map = {'A': True, 'B': False, 'C': True}
    result = evaluate_boolean_expression(expr, vars_map)
    print(result)